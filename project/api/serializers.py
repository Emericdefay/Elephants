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

    def get_html(self, obj):
        data = render_to_string(template_name='circuit_modal.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('category'),
                                    'actual_commands': Command.objects.filter(id=obj.id).order_by('client'),
                                })
        return mark_safe(data)
    
    def get_title(self, obj):
        return Circuit.objects.get(id=self.context['request']._request.GET.get('circuit')).name

    class Meta:
        model = Command
        fields = (
            'html',
            'title',
        )

class DayByDayCommandTotalSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    def get_html(self, obj):
        day_date_command=(self.context['request']._request.GET.get('day_date_command'))
        month_date_command=(self.context['request']._request.GET.get('month_date_command'))
        year_date_command=(self.context['request']._request.GET.get('year_date_command'))
        data = render_to_string(template_name='circuit_unit_total.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('category'),
                                    'day': day_date_command,
                                    'month': month_date_command,
                                    'year': year_date_command,
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
                                    'foods': Food.objects.all().order_by('category'),
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
