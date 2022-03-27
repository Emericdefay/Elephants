# Local libs
import json
import operator
import logging
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
from .models import Food, Client, Circuit, Command, DefaultCommand, FoodCategory
from .forms import ClientForm, CircuitForm, DefaultCommandForm, CommandForm
from .serializers import ClientSerializer, CommandSerializer


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
        gradients_colors = {(circuit.id, gradients[index]) for index, circuit in enumerate(circuits)}
        # Planning tab
        days = list(range(1, 32))
        commands = list(Command.objects.all())
        # Food tab
        foods = Food.objects.all().order_by('category')
        foodcategories = FoodCategory.choices
        # Tools

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
            'days': days,
            'foodcategories': foodcategories,
            'gradients': gradients_colors,
            'defaultcommands': (defaultcommands),
        }
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        context['formClient'] = form['clients']
        context['formCircuit'] = form['circuits']
        context['formDefaultCommand'] = form['defaultcommands']
        context['gradients'] = form['gradients']
        context['year'] = kwargs['year'] if 'year' in kwargs else datetime.now().year
        context['month'] = kwargs['month'] if 'month' in kwargs else datetime.now().month
        context['days'] = form['days']
        context['foods'] = form['foods']
        context['foodcategories'] = form['foodcategories']

        all_objects = [*Command.objects.all(), *Client.objects.all()]
        data = serializers.serialize('json', all_objects)

        context['data'] = data

        
        return context

    def object(self, *args, **kwargs):
        return super().object(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
