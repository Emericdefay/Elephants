from datetime import datetime
from click import command
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models import F, FloatField, Q
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.formats import date_format
from django.utils.safestring import mark_safe
from rest_framework import serializers

from project.manager.choices import CommandTimes
from project.manager.models import Command, Food, WeekRange, Client, DefaultCommand, Circuit


class DayByDayCommandSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    food = serializers.SerializerMethodField()

    def get_html(self, obj):
        data = render_to_string(template_name='circuit_modal.html',
                                context={
                                    'commands': obj,
                                    'client_id': obj.client.id,
                                    'foods': Food.objects.all().order_by('id'),
                                    'actual_commands': Command.objects.filter(id=obj.id).order_by('client'),
                                })
        return mark_safe(data)
    
    def get_title(self, obj):
        circuit = self.context['request']._request.GET.get('circuit') or self.context['request']._request.GET.get('circuit_id')
        return Circuit.objects.get(id=circuit).name

    def get_id(self, obj):
        return obj.client.id

    def get_food(self, obj):
        number_commanded = Command.objects.get(id=obj.id).command_command
        return [(food, number_commanded) for food in Command.objects.filter(id=obj.id).order_by('client').values_list('meals', flat=True)]


    class Meta:
        model = Command
        fields = (
            'id',
            'html',
            'title',
            'food',
        )


class DayByDayCommandTotalSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    def get_html(self, obj):       
        data = render_to_string(template_name='circuit_unit_total.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('id'),
                                    'search': self.context['request']._request.GET.get('search'),
                                    'actual_commands': Command.objects.filter(id=obj.id).order_by('client'),
                                })
        return mark_safe(data)

    class Meta:
        model = Command
        fields = (
            'html',
        )


class DayByDayCircuitSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    html = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    food = serializers.SerializerMethodField()
    circuit = serializers.SerializerMethodField()


    def get_id(self, obj):
        return f'total-circuit-{obj.client.circuit.id}-{obj.day_date_command}'

    def get_html(self, obj):
        data = render_to_string(template_name='circuit_total.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('id'),
                                    'actual_commands': Command.objects.filter(id=obj.id).order_by('client'),
                                })
        return mark_safe(data)

    def get_food(self, obj):
        number_commanded = Command.objects.get(id=obj.id).command_command
        return [(food, number_commanded) for food in Command.objects.filter(id=obj.id).order_by('client').values_list('meals', flat=True)]


    def get_title(self, obj):
        return "Récapitulatif"

    def get_circuit(self, obj):
        return obj.client.circuit.id

    class Meta:
        model = Command
        fields = (
            'html',
            'id',
            'title',
            'food',
            'circuit',
        )


class DayByDayCircuitTotalSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    def get_html(self, obj):
        data = render_to_string(template_name='circuit_total_total.html',
                                context={
                                    'commands': obj,
                                    'search': self.context['request']._request.GET.get('search'),
                                    'foods': Food.objects.all().order_by('id'),
                                    'actual_commands': Command.objects.filter(id=obj.id).order_by('client'),
                                })
        return mark_safe(data)
    

    class Meta:
        model = Command
        fields = (
            'html',
        )


class AllCommentsOfCustomerSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    client_id = serializers.SerializerMethodField()
    command_id = serializers.SerializerMethodField()
    day = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()


    def get_html(self, obj):
        data = render_to_string(template_name='customer_comment.html',
                                context={
                                    'commands': obj,
                                })
        return mark_safe(data)

    def get_client_name(self, obj):
        return f"{obj.client.last_name} {obj.client.first_name}"

    def get_client_id(self, obj):
        return obj.client.id

    def get_command_id(self, obj):
        return obj.id

    def get_day(self, obj):
        return obj.day_date_command

    def get_month(self, obj):
        return obj.month_date_command

    def get_year(self, obj):
        return obj.year_date_command

    class Meta:
        model = Command
        fields = (
            'html',
            'client_name',
            'client_id',
            'command_id',
            'day',
            'month',
            'year',
        )


class ClientDefaultFoodSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    html_food = serializers.SerializerMethodField()

    def get_html(self, obj):

        data = render_to_string(template_name='client_default_food.html',
                                context={
                                    'is_food_html': False,
                                    'is_different_from_default': obj.is_different_from_default,
                                    'client_command_food': obj.meals.all(),
                                    'all_foods': DefaultCommand.objects.all().order_by('order_food'),
                                })
        return mark_safe(data)

    def get_html_food(self, obj):

        data = render_to_string(template_name='client_default_food.html',
                                context={
                                    'is_food_html': True,
                                    'is_different_from_default': obj.is_different_from_default,
                                    'client_command_food': obj.client.client_command.all(),
                                    'all_foods': DefaultCommand.objects.all().order_by('order_food'),
                                })
        return mark_safe(data)

    class Meta:
        model = Command
        fields = (
            'html',
            'html_food',
        )


class GetAllClientsSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    def get_html(self, obj):
        circuits = Circuit.objects.all().order_by('name')
        month=self.context['request']._request.GET.get('month', datetime.now().month)
        year=self.context['request']._request.GET.get('year', datetime.now().year)
        if year == '0':
            year = datetime.now().year
        if month == '0':
            month = datetime.now().month
        data = render_to_string(template_name='tr_client.html',
                                context={
                                    'circuits': circuits.order_by('order_c'),
                                    'actual_month': str(month),
                                    'actual_year': str(year),
                                    'client': obj,
                                    'commands': Command.objects.filter(month_date_command=month, year_date_command=year, client=obj),
                                    'all_foods': DefaultCommand.objects.all().order_by('order_food'),
                                })
        return mark_safe(data)

    class Meta:
        model = Command
        fields = (
            'html',
        )