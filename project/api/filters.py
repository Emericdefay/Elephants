from email.policy import default
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from project.manager.models import Command, Circuit, Client


class DayByDayCommandFilter(filters.FilterSet):

    day_date_command = filters.NumberFilter(
        label="day",
    )
    month_date_command = filters.NumberFilter(
        label="month",
    )
    year_date_command = filters.NumberFilter(
        label="year",
    )
    circuit_id = filters.ModelChoiceFilter(
        label="circuit",
        queryset=Circuit.objects.all(),
    )


    class Meta:
        model = Command
        fields = [
            'day_date_command',
            'month_date_command',
            'year_date_command',
            'circuit_id',
        ]


class CommandCustomerFilter(filters.FilterSet):

    client_id = filters.ModelChoiceFilter(
        label="circuit",
        queryset=Client.objects.all(),
    )


    class Meta:
        model = Command
        fields = [
            'client_id',
        ]
