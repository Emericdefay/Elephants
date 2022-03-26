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
from django.views.generic import TemplateView, DetailView
from django.views.generic.dates import timezone_today
from django.shortcuts import render
# app libs


class HomeView(TemplateView):
    template_name = 'manager/index.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

