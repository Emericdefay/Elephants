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

    def get_id(self, obj):
        return f'total-circuit-{obj.circuit.id}'

    def get_html(self, obj):
        data = render_to_string(template_name='circuit_total.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('id'),
                                    'actual_commands': Command.objects.filter(id=obj.id).order_by('client'),
                                })
        return mark_safe(data)
    
    def get_title(self, obj):
        return "Récapitulatif"

    class Meta:
        model = Command
        fields = (
            'html',
            'id',
            'title',
        )


class DayByDayCircuitTotalSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    def get_html(self, obj):
        data = render_to_string(template_name='circuit_total_total.html',
                                context={
                                    'commands': obj,
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

    def get_html(self, obj):
        data = render_to_string(template_name='customer_comment.html',
                                context={
                                    'commands': obj,
                                })
        return mark_safe(data)

    def get_client_name(self, obj):
        return f"{obj.client.last_name} {obj.client.first_name}"

    class Meta:
        model = Command
        fields = (
            'html',
            'client_name',
        )
