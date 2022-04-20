from django.db.models import F, FloatField, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.dates import timezone_today
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets, renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from project.manager import models
from . import serializers, filters


# Create your views here.
class DayByDayCommand(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCommandSerializer

    def get_queryset(self):
        # get non expired ads
        qs = models.Command.objects.filter(
            client__circuit_id=self.request._request.GET.get('circuit'),
            day_date_command=self.request._request.GET.get('day_date_command'),
            month_date_command=self.request._request.GET.get('month_date_command'),
            year_date_command=self.request._request.GET.get('year_date_command'),
            ).order_by('client__order')
        return qs


# Create your views here.
class DayByDayCommandTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCommandTotalSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        qs = models.Command.objects.filter(
            client__circuit_id=self.request._request.GET.get('circuit'),
            day_date_command=self.request._request.GET.get('day_date_command'),
            month_date_command=self.request._request.GET.get('month_date_command'),
            year_date_command=self.request._request.GET.get('year_date_command'),
            )

        return qs

# Create your views here.
class DayByDayCircuitTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCircuitSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        return models.Command.objects.all().distinct().order_by('circuit')