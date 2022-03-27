# Local libs
import json
import logging
from datetime import timedelta
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
from .models import Food, Client, Circuit, Command, Planning
from .forms import ClientForm, CircuitForm
from .serializers import ClientSerializer


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
        clients = Client.objects.all().order_by('last_name', 'first_name')
        circuits = Circuit.objects.all().order_by('name')
        print(circuits)
        form = {
            'clients':({(ClientForm(instance=(client))) for client in (clients)}),
            'circuits':({(CircuitForm(instance=(circuit))) for circuit in (circuits)}),
        }
        return form

    def get_circuit_form(self):
        """ form for setting the status of a synergy """
        circuits = Circuit.objects.all()
        return ({(CircuitForm(instance=(circuit))) for circuit in (circuits)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['formClient'] = self.get_form()['clients']
        context['formCircuit'] = self.get_form()['circuits']
        return context

    def object(self):
        pass

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
