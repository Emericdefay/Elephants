# Local libs
import json
import operator
import logging
from calendar import monthrange
import locale
from datetime import timedelta, datetime
from pickletools import floatnl
from django.core import serializers
# django libs
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q, OuterRef, Exists
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView
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

    def post(self, request, *args, **kwargs):
        """_summary_
        """
        save = self.request._post
        save2 = self.request.__dict__
        form = request.POST.get('')
        print("---------------")
        print(save)
        print("---------------")
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
        context['morning_evening'] = ["morning", "evening"]
        context['actual_week'] = 9


        existing_clients = Client.objects.all()

        # TODO : Optimiser la génération des commandes : ne prendre que les 
        #        commandes existantes et créer les nouvelles uniquement après
        #        ajouts de morning/evening commands.
        for index, client in enumerate(existing_clients):
            for day in context['days']:
                Command.objects.get_or_create(
                    client=client,
                    morning_command=0,
                    evening_command=0,
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

        clients_commands = {
            'client':'a'
        }

        clients = Client.objects.all().order_by('circuit')
        context['clients'] =clients

        all_objects = [*Command.objects.all().order_by('client__circuit'), *Client.objects.all()]
        data = serializers.serialize('json', all_objects)
        context['data'] = commands
        return context

    def object(self, *args, **kwargs):
        return super().object(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateWeekRange(UpdateView):

 
    def post(self, request, *args, **kwargs):
        week_range = WeekRange.objects.get(id=1)
        print(f"range : {self.request.__dict__}")
        print(f"range : {self.request._post}")
        print(self.request._post['week_range_input'])
        print(args)
        print(kwargs)
        week_range.range = self.request._post['week_range_input']
        week_range.save()


        return redirect(reverse('manager:index'))