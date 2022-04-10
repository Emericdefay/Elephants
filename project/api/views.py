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
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        qs = models.Command.objects.all()

        return qs.distinct().order_by('circuit')

# Create your views here.
class DayByDayCommandTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCommandTotalSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        qs = models.Command.objects.all()

        return qs.distinct().order_by('circuit')

# Create your views here.
class DayByDayCircuitTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    serializer_class = serializers.DayByDayCircuitSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        query = models.Command.objects.all().distinct().order_by('circuit')
        copy1 = []
        copy2 = []
        for data in query:
            if data.circuit not in copy1:
                copy1.append(data.circuit)
                copy2.append(data)
            query = copy2
        qs = models.Command.objects.filter(id__in={instance.id for instance in query})
        return qs