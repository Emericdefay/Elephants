from email.policy import default
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from django.db.models import Q
from django.forms import widgets

from project.manager.models import Command, Circuit, Client
from project.manager import models


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

    search = filters.CharFilter(label='', method='custom_search',
                                widget=widgets.TextInput(attrs={
                                    "placeholder": _("What are you looking for ?")
                                }))

    def custom_search(self, queryset, name, value):
        circuit = self.request._request.GET.get('circuit') or self.request._request.GET.get('circuit_id')
        if value:
            # search in description or ad tags

            try:
                qs = models.Command.objects.filter(
                    command_command__gt=0,
                    day_date_command__in=self.request._request.GET.get('day_date_command__in'),
                    month_date_command=self.request._request.GET.get('month_date_command'),
                    year_date_command=self.request._request.GET.get('year_date_command'),
                    ).order_by('client__order')
                if circuit:
                    qs = qs.filter(client__circuit_id=circuit).order_by('client__order')

                return qs
            except:
                try:
                    dayone, daytwo = self.request._request.GET.get('search').split(',')[0], self.request._request.GET.get('search').split(',')[1]
                    qs = models.Command.objects.none()
                    qs |= models.Command.objects.filter(
                        command_command__gt=0,
                        day_date_command__in=[dayone.split('-')[0]],
                        month_date_command=dayone.split('-')[1],
                        year_date_command=dayone.split('-')[-1],
                        ).order_by('client__order')
                    qs |= models.Command.objects.filter(
                        command_command__gt=0,
                        day_date_command__in=[daytwo.split('-')[0]],
                        month_date_command=daytwo.split('-')[1],
                        year_date_command=daytwo.split('-')[-1],
                        ).order_by('client__order')
                    if circuit:
                        qs = qs.filter(client__circuit_id=circuit).order_by('client__order')
                    return qs

                except IndexError:
                    dayone = self.request._request.GET.get('search')
                    qs = models.Command.objects.filter(
                        command_command__gt=0,
                        day_date_command__in=[dayone.split('-')[0]],
                        month_date_command=dayone.split('-')[1],
                        year_date_command=dayone.split('-')[-1],
                        ).order_by('client__order')
                    if circuit:
                        qs = qs.filter(client__circuit_id=circuit).order_by('client__order')
                    return qs
        return queryset

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


class ClientFilter(filters.FilterSet):

    id = filters.NumberFilter(
        label="id",
    )

    class Meta:
        model = Client
        fields = [
            'id',
        ]

class CommandFilter(filters.FilterSet):

    id = filters.NumberFilter(
        label="id",
    )

    class Meta:
        model = Command
        fields = [
            'id',
        ]
