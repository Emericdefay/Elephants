from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models import F, FloatField, Q
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.formats import date_format
from django.utils.safestring import mark_safe
from rest_framework import serializers

from project.manager.choices import CommandTimes
from project.manager.models import Command, Food, WeekRange, Client


class DayByDayCommandSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    def get_html(self, obj):
        request = self.context.get('request')
        existing_clients = Client.objects.filter(circuit=obj.circuit)
        actual_commands = Command.objects.none()
        for index, client in enumerate(existing_clients):
            actual_commands |= Command.objects.filter(
                Q(client=client)&
                Q(circuit=obj.circuit)&
                Q(day_date_command=obj.day_date_command)&
                Q(month_date_command=obj.month_date_command)&
                Q(year_date_command=obj.year_date_command)
            )

        data = render_to_string(template_name='circuit_modal.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('category'),
                                    'actual_commands': actual_commands.order_by('client'),
                                })
        return mark_safe(data)

    class Meta:
        model = Command
        fields = (
            'html',
        )

class DayByDayCommandTotalSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    def get_html(self, obj):
        request = self.context.get('request')
        existing_clients = Client.objects.filter(circuit=obj.circuit)
        actual_commands = Command.objects.none()
        for index, client in enumerate(existing_clients):
            actual_commands |= Command.objects.filter(
                Q(client=client)&
                Q(circuit=obj.circuit)&
                Q(day_date_command=obj.day_date_command)&
                Q(month_date_command=obj.month_date_command)&
                Q(year_date_command=obj.year_date_command)
            )

        data = render_to_string(template_name='circuit_unit_total.html',
                                context={
                                    'commands': obj,
                                    'foods': Food.objects.all().order_by('category'),
                                    'actual_commands': actual_commands.order_by('client'),
                                })
        return mark_safe(data)

    class Meta:
        model = Command
        fields = (
            'html',
        )

