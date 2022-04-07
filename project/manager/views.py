# Local libs
import json
import operator
import logging
from calendar import monthrange
import locale
from datetime import timedelta, datetime
import isoweek
import datetime as datetime_
from dateutil.relativedelta import relativedelta
from pickletools import floatnl
# django libs
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q, OuterRef, Exists
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView
from django.views.generic.dates import timezone_today
from django.shortcuts import render
# app libs
from .models import Food, Client, Circuit, Command, DefaultCommand, FoodCategory, WeekRange
from .forms import ClientForm, CircuitForm, DefaultCommandForm, CommandForm, FoodForm
from .serializers import ClientSerializer, CommandSerializer
from django.utils import translation
from django.utils.translation import gettext as _
translation.activate('fr')


class UpdateHomeView(View):
    """ update the status of the synergy """

    def synth_client(self, save):
        """ INFO CLIENT """
        targets = ['order', 'last_name', 'first_name', 'circuit_id', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets and len(str(key).split('__')) == 2:
                key_values.update({key: value})
        # detect id
        ids = set()
        for i in key_values.keys():
            ids.add(i.split('__')[1])
        # regroup by id
        values_by_id = dict()
        for id_ in ids:
            values_by_id[id_] = {key.split('__')[0]:value for key, value in key_values.items() if key.split('__')[1]==id_}
        # save
        for client_id, kwargs in values_by_id.items():
            Client.objects.filter(id=client_id).update(**kwargs)
        """ MEALS """
        targets = ['_meals', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets:
                key_values.update({key: value})
        # select values
        values_by_id = dict()
        for id_ in ids:
            values_by_id[id_] = [key.split('__')[1] for key in key_values.keys() if key.split('__')[-1] == id_]
        # checks
        for id_ in ids:
            for food in DefaultCommand.objects.all():
                Client.objects.get(id=id_).client_command.remove(food)
            for food in DefaultCommand.objects.filter(id__in=values_by_id[id_]):
                Client.objects.get(id=id_).client_command.add(food)

    def post(self, request, *args, **kwargs):
        """_summary_
        """
        save = self.request._post
        save2 = self.request.__dict__
        form = request.POST.get('')
        print("---------------")
        for key, values in save.items():
            #print(f"{key} : {values}")
            pass
        print("---------------")
        # save client /1
        self.synth_client(save)
        print("---------------")

        # Clients
        # last_name
        # first_name
        # client_command
        # circuit
        # order

        return redirect(reverse('manager:index'))


class DeleteUser(View):
    """_summary_
    """
    def post(self, request, *args, **kwargs):
        """
        """
        return redirect(reverse('manager:index'))
        

class HomeView(TemplateView, UpdateView):
    template_name = 'manager/index.html'

    def get_form(self):
        """ form for setting the status of a synergy """
        # Client tab
        clients = Client.objects.all().order_by('circuit', 'last_name', 'first_name')
        circuits = Circuit.objects.all().order_by('name')
        defaultcommands = DefaultCommand.objects.all().order_by('default')
        gradients = [f'#{(hex(int(256*256*256 - (250*250*250)//(k+1) )))[2:]}' for k in range(len(list(circuits)))]
        gradients_colors = dict((circuit.id, gradients[index]) for index, circuit in enumerate(circuits))
        # Planning tab
        commands = list(Command.objects.all())
        # Food tab
        foods = Food.objects.all().order_by('category')
        foodcategories = FoodCategory.choices
        # Tools
        week_range = WeekRange.objects.get_or_create(id=1)

        form = {
            # CLIENTS
            'clients': ((ClientForm(instance=(client))) for client in list(clients)),
            # CIRCUITS
            'circuits':({(CircuitForm(instance=(circuit))) for circuit in list(circuits)}),
            # FOOD
            'foods': foods,
            # COMMANDS
            'commands': commands,
            # Tools
            'foodcategories': foodcategories,
            'gradients': gradients_colors,
            'defaultcommands': (defaultcommands),
            'week_range': week_range,
            'new_client': ClientForm()
        }
        return form

    def set_locale(self, locale_):
        locale.setlocale(category=locale.LC_ALL, locale=locale_)

    def date_customerprofile(self, context):
        return [_(datetime(context['year'], context['month'], day).strftime("%A")) for day in context['days']]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        context['formClient'] = form['clients']
        context['formCircuit'] = form['circuits']
        context['formDefaultCommand'] = form['defaultcommands']
        context['gradients'] = form['gradients']
        context['year'] = kwargs['year'] if 'year' in kwargs else datetime.now().year
        context['month'] = kwargs['month'] if 'month' in kwargs else datetime.now().month
        context['days'] = list(range(1, 20))#monthrange(context['year'], context['month'])[1] + 1))
        context['days_name'] = self.date_customerprofile(context)
        context['foods'] = form['foods']
        context['foodcategories'] = form['foodcategories']
        circuits = Circuit.objects.all().order_by('name')
        context['circuits'] = circuits
        gradients = gradients = [f'#{(hex(int(256*256*256 - (250*250*250)//(k+1) )))[2:]}' for k in range(len(list(circuits)))]
        context['circuits_colors'] = [(gradients[index]) for index, circuit in enumerate(circuits)]
        context['actual_week'] = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day,
            ).isocalendar()[1]
        context['actual_year'] = kwargs['year'] if 'year' in kwargs else datetime.now().year

        existing_clients = Client.objects.all()
        # TODO : Optimiser la génération des commandes : ne prendre que les 
        #        commandes existantes et créer les nouvelles uniquement après
        #        ajouts de commandes.
        for index, client in enumerate(existing_clients):
            for day in context['days']:
                Command.objects.get_or_create(
                    client=client,
                    day_date_command=day,
                    month_date_command=kwargs['month'] if 'month' in kwargs else datetime.now().month,
                    year_date_command=kwargs['year'] if 'year' in kwargs else datetime.now().year,
                )

        context['week_range'] = form['week_range']
        context['week_range_choices'] = list(range(0, 4))

        commands = Command.objects.filter(
            Q(month_date_command=(kwargs['month'] if 'month' in kwargs else datetime.now().month))
            & Q(year_date_command=(kwargs['year'] if 'year' in kwargs else datetime.now().year))
            ).order_by('client')
        context['data'] = commands

        clients = Client.objects.all().order_by('circuit', 'order')
        context['clients'] =clients

        week_ = datetime.now().weekday
        date_origin = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day
            )
        week_range = WeekRange.objects.get(id=1).range
        date_ending = date_origin + relativedelta(weeks=+week_range)
        date_start = date_origin
        if week_range > 2:
            date_start = date_origin + relativedelta(weeks=-1)
            date_ending = date_origin + relativedelta(weeks=+(week_range-1))
        
        range_dates = [date_start + datetime_.timedelta(days=x) for x in range(0, (date_ending - date_start).days + 1)]
        context['range_dates'] = range_dates
        
        actual_commands = Command.objects.none()
        for index, client in enumerate(existing_clients):
            for date in range_dates:
                actual_commands |= Command.objects.filter(
                    Q(client=client)&
                    Q(day_date_command=date.day)&
                    Q(month_date_command=date.month)&
                    Q(year_date_command=date.year)
                )
        context['actual_commands'] = actual_commands.order_by('client')

        years_weeks = dict()
        for year in range(2020, 2050):
            years_weeks[year] = list()
            all_weeks = list({
                            week
                            for week in range(0, isoweek.Week.last_week_of_year(year).week + 1)
                             })
            years_weeks[year].append(all_weeks)
        
        date_origin = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day
            )
        list_weeks = list()
        for week in range(-52, 53):
            list_weeks.append(date_origin + relativedelta(weeks=+(week)))

        context['list_weeks'] = list_weeks

        range_weeks = list({x.isocalendar()[1] for x in range_dates})
        context['range_weeks'] = range_weeks

        context['new_client'] = form['new_client']

        return context

    def object(self, *args, **kwargs):
        return super().object(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateWeekRange(UpdateView):
    def post(self, request, *args, **kwargs):
        week_range = WeekRange.objects.get(id=1)
        week_range.range = self.request._post['week_range_input']
        week_range.save()
        return redirect(reverse('manager:index') + "?tab=#planning-tab")

class AddNewClient(CreateView):
    model = Client
    fields = [
        'first_name','last_name','address',
	    'cellphone','description', 'circuit'
        ]
    success_url = reverse_lazy('manager:index')