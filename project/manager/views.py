# Local libs
import os
import json
import operator
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
from .models import Food, Client, Circuit, Command, DefaultCommand, FoodCategory, WeekRange
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
        targets = ['order', 'last_name', 'first_name', 'circuit_id', 'address', 'postcode', 'cellphone', 'cellphone2']
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
        for client_id, kwargs in values_by_id.items():
            Client.objects.filter(id=client_id).update(**kwargs)
        """ MEALS """
        #print("--- %s seconds save1---" % (time.time() - start_time))
        targets = ['_meals', ]
        key_values = {}
        for key, value in save.items():
            if str(key).split('__')[0] in targets:
                key_values.update({key: value})
        # select values
        values_by_id = dict()
        for id_ in ids:
            values_by_id[id_] = [key.split('__')[1] for key in key_values.keys() if key.split('__')[-1] == id_]
        #
        # checks
        for id_ in ids:
            for food in DefaultCommand.objects.all():
                if str(food.id) in values_by_id[id_]:
                    if Client.objects.filter(id=id_).filter(client_command__in=[food]):
                        continue
                    Client.objects.get(id=id_).client_command.add(food)
                    continue
                Client.objects.get(id=id_).client_command.remove(food)
        #print("--- %s seconds save2---" % (time.time() - start_time))

    def synth_planning(self, save):
        """ PLANNING INFO """
        targets = ['command_command', 'comment', ]
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
        for key, value in values_by_id_2.items():
            if value != '' or value != None:
                command_id = key[-1]
                try:
                    command = Command.objects\
                                        .get(
                                            id=command_id,
                                        )
                    command.command_command = value
                    command.comment = value
                    command.save(update_fields=[key[0]])
                except ValueError as e:
                    pass
        targets = ['meals', ]
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
        values_by_id = dict()
        values_by_id = {(key.split('__')[0], key.split('__')[1], key.split('__')[3]):value for key, value in key_values.items()}
        # save
        # print(values_by_id)
        dict_list_food = dict()
        for key, value in values_by_id.items():
            dict_list_food[key[-1]] = []
        for key, value in values_by_id.items():
            dict_list_food[key[-1]].append(int(key[1]))
        dict_list_food_2 = dict()
        for key in list(Command.objects.filter(command_command__gt=0).values_list('id', flat=True)):
            try:
                dict_list_food_2.update(
                    {
                        str(key): dict_list_food[str(key)]
                    }
                )
            except:
                pass
        #print({ key: dict_list_food[key] for keykey in  })
        for id_ in dict_list_food_2.keys():
            for food in DefaultCommand.objects.all():
                if food.id in dict_list_food_2[id_]:
                    if Command.objects.filter(id=id_).filter(meals__in=[food]):
                        continue
                    Command.objects.get(id=id_).meals.add(food)
                    continue
                Command.objects.get(id=id_).meals.remove(food)

    def synth_food(self, save):
        """ INFO CLIENT """
        targets = ['price', 'category', ]
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


    def post(self, request, *args, **kwargs):
        """_summary_
        """
        print("\nSauvegarde", end="")
        start_time = time.time()
        # Getting saves
        save = self.request._post
        print(".", end="")
        # save client
        self.synth_client(save)
        print(".", end="")
        # save planning
        self.synth_planning(save)
        print(".", end="")
        # save food
        self.synth_food(save)
        print(".", end=" ")
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
        context['actual_month'] = kwargs['month'] if 'month' in kwargs else datetime.now().month

        context['actual_day'] = datetime_.date(
            kwargs['year'] if 'year' in kwargs else datetime.now().year,
            kwargs['month'] if 'month' in kwargs else datetime.now().month,
            kwargs['day'] if 'day' in kwargs else datetime.now().day,
            )


        existing_clients = Client.objects.all().order_by('circuit', 'order').values_list('id', flat=True)

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
        
        range_dates = [date_start + datetime_.timedelta(days=x) for x in range(0, (date_ending - date_start).days + 2)]
        context['range_dates'] = range_dates
        range_days = [date.day for date in range_dates]
        
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("Phase 2 :", end=" ")
        start_time = time.time()

        cut_actual_commands = []
        actual_commands = Command.objects.none()
        for client_id in list(existing_clients):
            if actual_commands.count() > 400:
                cut_actual_commands.append(actual_commands.order_by( 'client', 'client__order', ))
                actual_commands = Command.objects.none()
            for date in range_dates:
                actual_commands |= Command.objects.filter(
                    Q(client_id=client_id)&
                    Q(day_date_command__in=range_days)&
                    Q(month_date_command=date.month)&
                    Q(year_date_command=date.year)
                )
        if actual_commands.count() > 0:
            cut_actual_commands.append(actual_commands.order_by( 'client', 'client__order', ))
        context['actual_commands'] = actual_commands.order_by( 'client', 'client__order', )
        context['cut_actual_commands'] = cut_actual_commands

        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        print("Phase 3 :", end=" ")
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

        # TODO : Optimiser la génération des commandes : ne prendre que les 
        #        commandes existantes et créer les nouvelles uniquement après
        #        ajouts de commandes.
        print("Phase 4 :", end=" ")
        start_time = time.time()

        for client_id in list(existing_clients):
            for day in range_dates:
                Command.objects\
                    .filter(
                    client_id=client_id,
                    day_date_command=day.day,
                    month_date_command=day.month,
                    year_date_command=day.year,
                    )\
                    .get_or_create(
                    defaults={
                        'client':Client.objects.get(id=client_id),
                        'circuit':Client.objects.get(id=client_id).circuit,
                        'day_date_command':day.day,
                        'month_date_command':day.month,
                        'year_date_command':day.year,
                    }
                )
        print("en %s secondes!\n" % round((time.time() - start_time), 2))
        context['new_client'] = form['new_client']
        context['new_food'] = form['new_food']
        context['new_circuit'] = form['new_circuit']
        context['month_commands'] = Command.objects.filter(
            year_date_command=kwargs['year'] if 'year' in kwargs else datetime.now().year,
            month_date_command=kwargs['month'] if 'month' in kwargs else datetime.now().month,
            )

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
	    'cellphone','description', 'postcode', 'circuit'
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
        'name', 'description_c',
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

    def init_sheet(self, sheet):
        # h1
        sheet['D24'] = "Total TTC"
        sheet['D24'].font = self.font_h1()
        sheet['E31'] = "07 63 42 08 54"
        sheet['E31'].font = self.font_h1()
        sheet['E31'].alignment = Alignment(horizontal="center")
        # h2
        sheet['E12'] = "Chambéry, le"
        sheet['E12'].font = self.font_h2()
        sheet['F12'] = f"{datetime.now().day}-{datetime.now().month}-{datetime.now().year}"
        sheet['F12'].font = self.font_h2()
        sheet['C14'] = f"{datetime.now().month}"
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
        sheet['E28'] = "Afin de toujours mieux répondre à vos attentes, nous mettons à"
        sheet['E28'].font = self.font_p2()
        sheet['E28'].alignment = Alignment(horizontal="center")
        sheet['E29'] = "votre disposition une ligne téléphonique dédiée à vos repas."
        sheet['E29'].font = self.font_p2()
        sheet['E29'].alignment = Alignment(horizontal="center")
        # foot
        sheet['E34'] = "SARL ELEPHANT"
        sheet['E34'].font = self.font_foot()
        sheet['E34'].alignment = Alignment(horizontal="center")
        sheet['E35'] = "1 Rue Claude Martin - 73000 CHAMBERY"
        sheet['E35'].font = self.font_foot()
        sheet['E35'].alignment = Alignment(horizontal="center")
        sheet['E36'] = "SIRET 45149094000017"
        sheet['E36'].font = self.font_foot()
        sheet['E36'].alignment = Alignment(horizontal="center")

        return sheet

    def post(self, request, *args, **kwargs):
        # init
        wb = Workbook()
        month = self.request.POST.get('month', datetime.now().month)
        year = self.request.POST.get('year', datetime.now().year)
        clients = Client.objects.all().order_by('circuit')
        commands = Command.objects.filter(year_date_command=year, month_date_command=month)

        for client in clients:
            # Elephant img added
            img = drawing.image.Image(os.path.join(os.getcwd(), 'project', 'static', 'img_elephant.png'))
            img.anchor = 'C3'
            img.height = 148
            img.width  = 115

            # Create sheet
            wb.create_sheet(f"{client.last_name} {client.first_name}")
            active_sheet = wb[f"{client.last_name} {client.first_name}"]
            active_sheet = self.init_sheet(active_sheet)

            # Insert image
            active_sheet.add_image(img)

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
            active_sheet['F21'] = TTC * (100-5.5) / 100
            active_sheet['F21'].font = self.font_h2()
            active_sheet['F22'] = TTC * 5.5 / 100
            active_sheet['F22'].font = self.font_h2()
            active_sheet['F24'] = TTC
            active_sheet['F24'].font = self.font_h2()

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
                'E': 14,
                'F': 8,
                'G': 4,
                'H': 20,
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
