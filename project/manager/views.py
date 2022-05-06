# Local libs
import os
import json
import operator
from itertools import islice
import logging
from calendar import monthrange
import locale
from datetime import timedelta, datetime
import isoweek
import datetime as datetime_
import time
from dateutil.relativedelta import relativedelta
from pickletools import floatnl
# django libs
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q, OuterRef, Exists
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView
from django.views.generic.dates import timezone_today
from django.shortcuts import render

# app libs
from .models import Food, Client, Circuit, Command, DefaultCommand, FoodCategory, WeekRange, Company
from .forms import ClientForm, CircuitForm, DefaultCommandForm, CommandForm, FoodForm

from django.db.models import FloatField
from django.db.models import Q, Sum, Prefetch, F, Avg, Case, When, Value
from . import forms
from .serializers import ClientSerializer, CommandSerializer
from django.utils import translation
from django.utils.translation import gettext as _
from openpyxl import Workbook, drawing
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
translation.activate('fr')


class UpdateHomeView(View):
    """ update the status of the synergy """

    def synth_client(self, save):
        """ INFO CLIENT """
        targets = ['order', 'circuit_id', ]
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
        #start_time = time.time()
        # save
        print("--- circuit saves ", end="")
        start_time = time.time()
        objs = []
        for client_id, kwargs in values_by_id.items():
            for key, value in kwargs.items():
                client = Client.objects.get(id=client_id)
                setattr(client, key, value)
                objs.append(client)
        Client.objects.bulk_update(objs, ['circuit_id'])
        
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("--- order saves ", end="")
        start_time = time.time()
        for obj in objs:
            obj.save(update_fields=["order"])
        print("en %s secondes!\n" % round((time.time() - start_time), 2))

        """ MEALS """
        # targets = ['_meals', ]
        # key_values = {}
        # for key, value in save.items():
        #     if str(key).split('__')[0] in targets:
        #         key_values.update({key: value})
        # # select values
        # values_by_id = dict()
        # for id_ in ids:
        #     values_by_id[id_] = [key.split('__')[1] for key in key_values.keys() if key.split('__')[-1] == id_]
        # #
        # # checks
        # for id_ in ids:
        #     client = Client.objects.filter(id=id_)
        #     client_get = Client.objects.get(id=id_)
        #     for food in DefaultCommand.objects.all():
        #         if str(food.id) in values_by_id[id_]:
        #             if client.filter(client_command__in=[food]):
        #                 continue
        #             client_get.client_command.add(food)
        #             continue
        #         client_get.client_command.remove(food)

    def synth_circuit(self, save):
        """ INFO CLIENT """
        targets = ['order_c']
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
        #start_time = time.time()
        # save
        objs = []
        for circuit_id, kwargs in values_by_id.items():
            for key, value in kwargs.items():
                client = Circuit.objects.get(id=circuit_id)
                setattr(client, key, value)
                objs.append(client)
        for obj in objs:
            obj.save(update_fields=["order_c"])

    def synth_planning(self, save):
        """ PLANNING INFO """
        targets = ['command_command', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets:
                key_values.update({key: value})
        # print(key_values)
        # detect id
        ids = set()
        for i in key_values.keys():
            ids.add(i.split('__')[-1])
        # print(ids)
        # regroup by id
        values_by_id_2 = dict()
        values_by_id_2 = {(key.split('__')[0], key.split('__')[2]):value for key, value in key_values.items()}
        # save
        print("--- save commands  ", end=" ")
        start_time = time.time()
        objs = []
        for key, value in values_by_id_2.items():
            if value != '' or value != None:
                command_id = key[-1]
                try:
                    command = Command.objects\
                                        .get(
                                            id=command_id,
                                        )
                    command.command_command = value
                    objs.append(command)
                except ValueError as e:
                    pass
        #Command.objects.bulk_update(objs, ['command_command'])
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        targets = ['comment', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets:
                key_values.update({key: value})
        # print(key_values)
        # detect id
        ids = set()
        for i in key_values.keys():
            ids.add(i.split('__')[-1])
        # print(ids)
        # regroup by id
        values_by_id_2 = dict()
        values_by_id_2 = {(key.split('__')[0], key.split('__')[2]):value for key, value in key_values.items()}
        # save
        print("--- save comment ", end=" ")
        start_time = time.time()
        objs = []
        for key, value in values_by_id_2.items():
            if value != '' or value != None:
                command_id = key[-1]
                try:
                    command = Command.objects\
                                        .get(
                                            id=command_id,
                                        )
                    command.comment = value
                    objs.append(command)
                except ValueError as e:
                    pass
        Command.objects.bulk_update(objs, ['comment'])
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("--- save meals ", end=" ")
        start_time = time.time()
        # targets = ['meals', ]
        # key_values = {}
        # for key, value in save.items():
        #     if str(key).split('__')[0] in targets:
        #         key_values.update({key: value})
        # # print(key_values)
        # # detect id
        # ids = set()
        # for i in key_values.keys():
        #     ids.add(i.split('__')[-1])
        # # print(ids)
        # # regroup by id
        # values_by_id = dict()
        # values_by_id = {(key.split('__')[0], key.split('__')[1], key.split('__')[3]):value for key, value in key_values.items()}
        # # save
        # # print(values_by_id)
        # dict_list_food = dict()
        # for key, value in values_by_id.items():
        #     dict_list_food[key[-1]] = []
        # for key, value in values_by_id.items():
        #     dict_list_food[key[-1]].append(int(key[1]))
        # dict_list_food_2 = dict()
        # for key in list(Command.objects.filter(command_command__gt=0).values_list('id', flat=True)):
        #     try:
        #         dict_list_food_2.update(
        #             {
        #                 str(key): dict_list_food[str(key)]
        #             }
        #         )
        #     except:
        #         pass
        # for id_ in dict_list_food_2.keys():
        #     for food in DefaultCommand.objects.all():
        #         if food.id in dict_list_food_2[id_]:
        #             if Command.objects.filter(id=id_).filter(meals=food):
        #                 continue
        #             Command.objects.get(id=id_).meals.add(food)
        #             continue
        #         Command.objects.get(id=id_).meals.remove(food)
        print("en %s secondes!\n" % round((time.time() - start_time), 2))

    def synth_food(self, save):
        """ INFO CLIENT """
        targets = ['price', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets and len(str(key).split('__')) == 2:
                key_values.update({key: value})
        # detect id
        ids = set()
        for i in key_values.keys():
            ids.add(i.split('__')[1])
        # # regroup by id
        values_by_id = dict()
        for id_ in ids:
            values_by_id[id_] = dict()

        for id_ in ids:
            for key, value in key_values.items():
                if key.split('__')[1]==id_:
                    values_by_id[id_].update({key.split('__')[0]: value})
        # save
        for food_id, kwargs in values_by_id.items():
            Food.objects.filter(id=food_id).update(**kwargs)

        targets = ['category', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets and len(str(key).split('__')) == 2:
                key_values.update({key: value})
        # detect id
        ids = set()
        for i in key_values.keys():
            ids.add(i.split('__')[1])
        # # regroup by id
        values_by_id = dict()
        for id_ in ids:
            values_by_id[id_] = dict()

        for id_ in ids:
            for key, value in key_values.items():
                if key.split('__')[1]==id_:
                    values_by_id[id_].update({key.split('__')[0]: value})
        # save
        for food_id, kwargs in values_by_id.items():
            food = Food.objects.get(id=food_id)
            food.category = kwargs.get('category')
            food.save()

        targets = ['order_food', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets and len(str(key).split('__')) == 2:
                key_values.update({key: value})
        # detect id
        ids = set()
        for i in key_values.keys():
            ids.add(i.split('__')[1])
        # # regroup by id
        values_by_id = dict()
        for id_ in ids:
            values_by_id[id_] = dict()

        for id_ in ids:
            for key, value in key_values.items():
                if key.split('__')[1]==id_:
                    values_by_id[id_].update({key.split('__')[0]: value})
        # save
        for food_id, kwargs in values_by_id.items():
            DefaultCommand.objects.filter(id=food_id).update(**kwargs)

    def synth_company(self, save):
        """ INFO COMPANY """
        targets = ['comment_comp', 'cellphone_comp', 'company_comp', 'address_comp', 'siret_comp', ]
        key_values = {}
        for key, value in save.items():
            if str(key) in targets:
                key_values.update({key: value})
        # save
        Company.objects.filter(id=1).update(**key_values)


    def post(self, request, *args, **kwargs):
        """_summary_
        """
        print("\nSauvegarde", end="\n")
        # Getting saves
        print("- Data saves ", end="")
        start_time = time.time()
        save = self.request._post
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        # save client
        print("- save client ", end="\n")
        start_time = time.time()
        self.synth_client(save)
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        # save circuit
        print("- save circuit ", end="")
        start_time = time.time()
        self.synth_circuit(save)
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        # save planning
        print("- save planning ", end="\n")
        start_time = time.time()
        self.synth_planning(save)
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        # save food
        print("- save food ", end="")
        start_time = time.time()
        self.synth_food(save)
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        # save company
        print("- save company ", end=" ")
        start_time = time.time()
        self.synth_company(save)
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        return redirect(reverse('manager:index') + save['date_link'][1:] + save['save_link'])


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
        defaultcommands = DefaultCommand.objects.all().order_by('order_food')
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
            'new_client': ClientForm(),
            'new_food': FoodForm(),
            'new_circuit': CircuitForm(),
        }
        return form

    def set_locale(self, locale_):
        locale.setlocale(category=locale.LC_ALL, locale=locale_)

    def date_customerprofile(self, context):
        return [_(datetime(context['year'], context['month'], day).strftime("%A")) for day in context['days']]

    def get_context_data(self, **kwargs):
        print("Phase 1 :", end=" ")
        start_time = time.time()

        context = super().get_context_data(**kwargs)
        form = self.get_form()
        context['formClient'] = form['clients']
        context['formCircuit'] = form['circuits']
        context['gradients'] = form['gradients']
        context['year'] = kwargs['year'] if 'year' in kwargs else datetime.now().year
        context['month'] = kwargs['month'] if 'month' in kwargs else datetime.now().month
        context['days'] = list(range(1, 20))#monthrange(context['year'], context['month'])[1] + 1))
        context['days_name'] = self.date_customerprofile(context)
        context['foods'] = Food.objects.all()
        # realign foods with defaultfood
        for food in Food.objects.all():
            DefaultCommand.objects.get_or_create(
                id=food.id,
                default=food,
            )
        context['foods_edit'] = Food.objects.all()
        context['formDefaultCommand'] = form['defaultcommands']
        context['foodcategories'] = form['foodcategories']
        circuits = Circuit.objects.all().order_by('order_c')
        context['circuits'] = circuits
        gradients = gradients = [f'#{(hex(int(256*256*256 - (250*250*250)//(k+1) )))[2:]}' for k in range(len(list(circuits)))]
        context['circuits_colors'] = [(gradients[index]) for index, circuit in enumerate(circuits)]
        context['actual_week'] = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day,
            ).isocalendar()[1]
        context['actual_year'] = kwargs['year'] if 'year' in kwargs else datetime.now().year
        context['actual_month'] = kwargs['month'] if 'month' in kwargs else datetime.now().month

        context['actual_day'] = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day,
            )

        existing_clients = Client.objects.all().order_by('last_name', 'first_name').values_list('id', flat=True)

        context['week_range'] = form['week_range']
        context['week_range_choices'] = list(range(0, 4))

        clients = Client.objects.all()
        context['clients'] = Client.objects.all().order_by('last_name', 'first_name')
        context['clients_alpha'] = clients.order_by('last_name', 'first_name')
        context['clients_order'] = clients.order_by('circuit__order_c', 'order')

        week_ = datetime.now().weekday
        date_origin = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day
        )
        date_origin = date_origin - timedelta(days = date_origin.weekday())
        week_range = WeekRange.objects.get(id=1).range
        date_ending = date_origin + relativedelta(weeks=+week_range)
        date_start = date_origin
        if week_range > 2:
            date_start = date_origin + relativedelta(weeks=-1)
            date_ending = date_origin + relativedelta(weeks=+(week_range-1))
        
        range_dates = [date_start + datetime_.timedelta(days=x) for x in range(0, (date_ending - date_start).days)]
        context['range_dates'] = range_dates
        range_days = {date.day for date in range_dates}
        range_months = {date.month for date in range_dates}
        range_years = {date.year for date in range_dates}
        
        # testing optimization purpose
        # for client_id in range(200):
        #     Client.objects.get_or_create(
        #         first_name=client_id,
        #         last_name=client_id,
        #         address=client_id,
        #         postcode=client_id,
        #         address_details=client_id,
        #         cellphone=client_id,
        #         cellphone2=client_id,
        #         order=client_id,
        #         circuit=Circuit.objects.get(id=1),
        #     )

        print("en %s secondes!\n" % round((time.time() - start_time), 2))

        # TODO : Optimiser la génération des commandes : ne prendre que les 
        #        commandes existantes et créer les nouvelles uniquement après
        #        ajouts de commandes.
        print("Phase 2 :", end=" ")
        start_time = time.time()  
        dict_days_clients_commands_dont_exist = dict()
        for client_id in list(existing_clients):
            for day in range_dates:
                if not Command.objects\
                    .filter(
                    client_id=client_id,
                    day_date_command=day.day,
                    month_date_command=day.month,
                    year_date_command=day.year,
                    )\
                    .exists():
                    dict_days_clients_commands_dont_exist[(client_id, day)] = {'day':day.day, 'month':day.month, 'year':day.year}
        batch_size = 1000
        objs = (Command(
            client=Client.objects.get(id=client_day[0]),
            circuit=Client.objects.get(id=client_day[0]).circuit,
            day_date_command=dates.get('day'),
            month_date_command=dates.get('month'),
            year_date_command=dates.get('year'),
            ) for client_day, dates in dict_days_clients_commands_dont_exist.items())
        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Command.objects.bulk_create(batch, batch_size)

        print("en %s secondes!\n" % round((time.time() - start_time), 2))

        print("Phase 3 :", end=" ")
        start_time = time.time()

        # planning cuts
        cut_actual_commands = []
        actual_commands = Command.objects.none()
        for client_id in list(existing_clients):
            for date in range_dates:
                actual_commands |= Command.objects\
                .filter(client_id=client_id)\
                .filter(day_date_command=date.day)\
                .filter(month_date_command=date.month)\
                .filter(year_date_command=date.year)\
                .exclude(client__circuit__id=5)
            cut_actual_commands.append(actual_commands.order_by( 'client__last_name', 'client__first_name',  ))
            actual_commands = Command.objects.none()

        context['cut_actual_commands'] = cut_actual_commands
        context['actual_commands'] = Command.objects\
                                            .filter(day_date_command__in=range_days)\
                                            .filter(month_date_command__in=range_months)\
                                            .filter(year_date_command__in=range_years).order_by( 'circuit__order_c', 'client', 'client__order', )

        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("Phase 4 :", end=" ")
        start_time = time.time()

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
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("Phase 5 :", end=" ")
        start_time = time.time()
        context['new_client'] = form['new_client']
        context['new_food'] = form['new_food']
        context['new_circuit'] = form['new_circuit']
        context['month_commands'] = Command.objects.filter(
            year_date_command=kwargs['year'] if 'year' in kwargs else datetime.now().year,
            month_date_command=kwargs['month'] if 'month' in kwargs else datetime.now().month,
            )

        context['company'] = Company.objects.get_or_create(id=1)[0]

        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("Generation de la page HTML")
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
        'first_name','last_name','address', 'address_details',
	    'cellphone', 'cellphone2', 'postcode', 'circuit'
        ]
    success_url = reverse_lazy('manager:index')


class AddNewFood(CreateView):
    model = Food
    fields = [
        'category', 'price'
        ]
    success_url = reverse_lazy('manager:index')


class AddNewCircuit(CreateView):
    model = Circuit
    fields = [
        'name',
        ]
    success_url = reverse_lazy('manager:index')


class CreateExcel(View):

    def font_h1(self):
        return Font(name='Times New Roman',
                    size=14,
                    bold=True,
                    italic=False,
                    vertAlign=None,
                    underline='none',
                    strike=False,
                    color='FF000000')

    def font_h2(self):
        return Font(name='Times New Roman',
                    size=12,
                    bold=True,
                    italic=False,
                    vertAlign=None,
                    underline='none',
                    strike=False,
                    color='FF000000')

    def font_p1(self):
        return Font(name='Times New Roman',
                    size=14,
                    bold=False,
                    italic=False,
                    vertAlign=None,
                    underline='none',
                    strike=False,
                    color='FF000000')
    def font_p2(self):
        return Font(name='Times New Roman',
                    size=12,
                    bold=False,
                    italic=False,
                    vertAlign=None,
                    underline='none',
                    strike=False,
                    color='FF000000')

    def font_foot(self):
        return Font(name='Times New Roman',
                    size=12,
                    bold=True,
                    italic=False,
                    vertAlign=None,
                    underline='none',
                    strike=False,
                    color='FF363742')

    def init_sheet(self, sheet, number):
        company = Company.objects.get(id=1)
        # h1
        sheet['D24'] = "Total TTC"
        sheet['D24'].font = self.font_h1()
        sheet['E32'] = company.cellphone_comp
        sheet['E32'].font = self.font_h1()
        sheet['E32'].alignment = Alignment(horizontal="center")
        # h2
        sheet['D12'] = "Chambéry, le"
        sheet['D12'].font = self.font_h2()
        sheet['C14'] = number
        sheet['C14'].font = self.font_h2()
        sheet['C16'] = "Nombre de repas"
        sheet['C16'].font = self.font_h2()
        sheet['C18'] = "Prix unitaire ttc"
        sheet['C18'].font = self.font_h2()
        # p1
        sheet['B14'] = "Facture N°"
        sheet['B14'].font = self.font_p1()
        sheet['D21'] = "Total HT"
        sheet['D21'].font = self.font_p1()
        sheet['D22'] = "TVA 5.5%"
        sheet['D22'].font = self.font_p1()
        # p2
        text = company.comment_comp
        number_of_lines = len(text) // 80 + 1
        initial_row = 28
        put_to_other_line = ''
        for row_offset in range(number_of_lines):
            text_line = put_to_other_line + text[row_offset * 80:(row_offset + 1) * 80]
            put_to_other_line = ''
            if text_line[-1] != ' ' and row_offset != number_of_lines - 1:
                put_to_other_line = text_line.split(' ')[-1]
                text_line = ' '.join(text_line.split(' ')[:-1])

            sheet[f'E{initial_row + row_offset}'] = text_line
            sheet[f'E{initial_row + row_offset}'].font = self.font_p2()
            sheet[f'E{initial_row + row_offset}'].alignment = Alignment(horizontal="center")
        # foot
        sheet['E34'] = company.company_comp
        sheet['E34'].font = self.font_foot()
        sheet['E34'].alignment = Alignment(horizontal="center")
        sheet['E35'] = company.address_comp
        sheet['E35'].font = self.font_foot()
        sheet['E35'].alignment = Alignment(horizontal="center")
        sheet['E36'] = company.siret_comp
        sheet['E36'].font = self.font_foot()
        sheet['E36'].alignment = Alignment(horizontal="center")

        return sheet

    def post(self, request, *args, **kwargs):
        # init
        wb = Workbook()
        month = self.request.POST.get('month', datetime.now().month)
        year = self.request.POST.get('year', datetime.now().year)
        print(month, year)
        date_posted = self.request.POST.get('date', "")
        if date_posted != "":
            dates = date_posted.split('-')
            date = '-'.join([dates[-1], dates[1], dates[0]])
        else:
            date = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
        clients = Client.objects.all().order_by('circuit')
        commands = Command.objects.filter(year_date_command=year, month_date_command=month)

        for client in clients:
            # Elephant img added
            img = drawing.image.Image(os.path.join(os.getcwd(), 'project', 'static', 'img_elephant.png'))
            img.anchor = 'C3'
            img.height = 148
            img.width  = 115

            # Create sheet
            wb.create_sheet(f"{client.id} - {client.last_name} {client.first_name}")
            active_sheet = wb[f"{client.id} - {client.last_name} {client.first_name}"]
            active_sheet = self.init_sheet(active_sheet, month)

            # Insert image
            active_sheet.add_image(img)

            # Insert date
            active_sheet['F12'] = date
            active_sheet['F12'].font = self.font_h2()

            # set clients address
            active_sheet['H8'] = f"{client.last_name} {client.first_name}"
            active_sheet['H8'].font = self.font_h1()
            active_sheet['H9'] = f"{client.address}"
            active_sheet['H10'] = f"{client.postcode}"
            active_sheet['H9'].alignment = Alignment(wrap_text=True, shrink_to_fit=False)

            # Number of meals
            number_of_meals = commands.filter(client=client, command_command__gt=0).aggregate(sum=Sum(F('command_command')))['sum']
            active_sheet['F16'] = number_of_meals if number_of_meals else 0
            active_sheet['F16'].font = self.font_h2()

            
            unit_price = Food.objects.filter(id__in=client.client_command.all()).aggregate(sum=(Sum(F('price'))))['sum']
            active_sheet['F18'] = unit_price if unit_price else 0
            active_sheet['F18'].font = self.font_h2()
            active_sheet['F18'].number_format = '#,##0.00€' 

            # TTC calc
            TTC = commands.filter(client=client)\
                    .aggregate(sum=Sum(
                        (F('meals__default__price')) * F('command_command'),
                        output_field=FloatField(),
                        )
                    )['sum']
            if not TTC:
                TTC = 0.0
            active_sheet['F24'] = TTC
            active_sheet['F24'].font = self.font_h2()
            active_sheet['F21'] = "=F24*(1-0.055)"
            active_sheet['F21'].font = self.font_h2()
            active_sheet['F22'] = "=F24*0.055"
            active_sheet['F22'].font = self.font_h2()

            # format €
            active_sheet['F21'].number_format = '#,##0.00€' 
            active_sheet['F22'].number_format = '#,##0.00€' 
            active_sheet['F24'].number_format = '#,##0.00€' 

            # dimensions
            dims = {
                'A': 5,
                'B': 13,
                'C': 4,
                'D': 10,
                'E': 5,
                'F': 10,
                'G': 4,
                'H': 25,
            }
            for col, value in dims.items():
                active_sheet.column_dimensions[col].width = value
            # Border on prices
            thin = Side(border_style="double")
            for number in range(21, 25):
                active_sheet[f'C{number}'].border = Border(left=thin)
                active_sheet[f'G{number}'].border = Border(right=thin)
            for letter in ['D', 'E', 'F']:
                active_sheet[f'{letter}20'].border = Border(top=thin)
                active_sheet[f'{letter}25'].border = Border(bottom=thin)
            active_sheet[f'C20'].border = Border(top=thin, left=thin)
            active_sheet[f'G20'].border = Border(top=thin, right=thin)
            active_sheet[f'C25'].border = Border(bottom=thin, left=thin)
            active_sheet[f'G25'].border = Border(bottom=thin, right=thin)
        # Delete std Sheet
        std = wb.get_sheet_by_name('Sheet')
        wb.remove_sheet(std)

        # Export
        response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="Factures_{month}_{year}.xlsx"'

        return response
