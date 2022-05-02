from django.db.models import F, FloatField, Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.dates import timezone_today
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets, renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from project.manager import models
from . import serializers, filters


class DayByDayCommand(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCommandSerializer
    filter_fields= ({
        'day_date_command': ["in", "exact"]
    })

    def get_queryset(self):
        # get non expired ads
        try:
            day_date_command__in = [int(day) for day in self.request._request.GET.get('day_date_command__in').split(',')]
            qs = models.Command.objects.filter(
                command_command__gt=0,
                client__circuit_id=self.request._request.GET.get('circuit'),
                day_date_command__in=day_date_command__in,
                month_date_command=self.request._request.GET.get('month_date_command'),
                year_date_command=self.request._request.GET.get('year_date_command'),
                ).order_by('client__order')
        except AttributeError:
            try:
                dayone, daytwo = self.request._request.GET.get('search').split(',')[0], self.request._request.GET.get('search').split(',')[1]
                qs = models.Command.objects.none()
                qs |= models.Command.objects.filter(
                    command_command__gt=0,
                    client__circuit_id=self.request._request.GET.get('circuit'),
                    day_date_command__in=[dayone.split('-')[0]],
                    month_date_command=dayone.split('-')[1],
                    year_date_command=dayone.split('-')[-1],
                    ).order_by('client__order')
                qs |= models.Command.objects.filter(
                    command_command__gt=0,
                    client__circuit_id=self.request._request.GET.get('circuit'),
                    day_date_command__in=[daytwo.split('-')[0]],
                    month_date_command=daytwo.split('-')[1],
                    year_date_command=daytwo.split('-')[-1],
                    ).order_by('client__order')
                return qs

            except IndexError:
                dayone = self.request._request.GET.get('search')
                qs = models.Command.objects.filter(
                    command_command__gt=0,
                    client__circuit_id=self.request._request.GET.get('circuit'),
                    day_date_command__in=[dayone.split('-')[0]],
                    month_date_command=dayone.split('-')[1],
                    year_date_command=dayone.split('-')[-1],
                    ).order_by('client__order')
        return qs


class DayByDayCommandTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCommandTotalSerializer
    queryset = models.Command.objects.none()
    filter_fields= ({
        'day_date_command': ["in", "exact"]
    })

    def get_queryset(self):
        try:
            day_date_command__in = [int(day) for day in self.request._request.GET.get('day_date_command__in').split(',')]
            qs = models.Command.objects.filter(
                command_command__gt=0,
                client__circuit_id=self.request._request.GET.get('circuit'),
                day_date_command__in=day_date_command__in,
                month_date_command=self.request._request.GET.get('month_date_command'),
                year_date_command=self.request._request.GET.get('year_date_command'),
                ).order_by('client__order')
        except AttributeError:
            try:
                dayone, daytwo = self.request._request.GET.get('search').split(',')[0], self.request._request.GET.get('search').split(',')[1]
                qs = models.Command.objects.none()
                qs |= models.Command.objects.filter(
                    command_command__gt=0,
                    client__circuit_id=self.request._request.GET.get('circuit'),
                    day_date_command__in=[dayone.split('-')[0]],
                    month_date_command=dayone.split('-')[1],
                    year_date_command=dayone.split('-')[-1],
                    ).order_by('client__order')
                qs |= models.Command.objects.filter(
                    command_command__gt=0,
                    client__circuit_id=self.request._request.GET.get('circuit'),
                    day_date_command__in=[daytwo.split('-')[0]],
                    month_date_command=daytwo.split('-')[1],
                    year_date_command=daytwo.split('-')[-1],
                    ).order_by('client__order')
                return qs

            except IndexError:
                dayone = self.request._request.GET.get('search')
                qs = models.Command.objects.filter(
                    command_command__gt=0,
                    client__circuit_id=self.request._request.GET.get('circuit'),
                    day_date_command__in=[dayone.split('-')[0]],
                    month_date_command=dayone.split('-')[1],
                    year_date_command=dayone.split('-')[-1],
                    ).order_by('client__order')
        return qs


class DayByDayCircuitTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCircuitSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        try:
            day_date_command__in = [int(day) for day in self.request._request.GET.get('day_date_command__in').split(',')]
            qs = models.Command.objects.filter(
                command_command__gt=0,
                day_date_command__in=day_date_command__in,
                month_date_command=self.request._request.GET.get('month_date_command'),
                year_date_command=self.request._request.GET.get('year_date_command'),
                ).order_by('client__order')
        except AttributeError:
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
                return qs

            except IndexError:
                dayone = self.request._request.GET.get('search')
                qs = models.Command.objects.filter(
                    command_command__gt=0,
                    day_date_command__in=[dayone.split('-')[0]],
                    month_date_command=dayone.split('-')[1],
                    year_date_command=dayone.split('-')[-1],
                    ).order_by('client__order')
        return qs


class DayByDayCircuitTotalTotal(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.DayByDayCommandFilter
    serializer_class = serializers.DayByDayCircuitTotalSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        return models.Command.objects.all().distinct().order_by('circuit')


class AllCommentsOfCustomer(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.CommandCustomerFilter
    serializer_class = serializers.AllCommentsOfCustomerSerializer
    queryset = models.Command.objects.none()

    def get_queryset(self):
        # get non expired ads
        return models.Command.objects\
            .filter(client_id=self.request._request.GET.get('client_id'))\
            .distinct()\
            .exclude(
                    comment='',
                    )\
            .exclude(
                    comment=None,
                    )\
            .exclude(
                    comment='None',
                    )\
            .order_by('year_date_command', 'month_date_command', 'day_date_command')


class CommandCommentUpdate(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return models.Command.objects.get(pk=pk)
        except models.Command.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        command = self.get_object(pk)
        command.comment = ""
        command.save()
        return Response(serializers.AllCommentsOfCustomerSerializer(command).data)


class ClientUpdate(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return models.Client.objects.get(pk=pk)
        except models.Command.DoesNotExist:
            raise Http404

    def get(self, request, pk, attr, value, format=None):
        client = self.get_object(pk)
        setattr(client, attr, value)
        client.save()
        return Response()

class ClientDefaultFoodUpdate(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return models.Client.objects.get(pk=pk)
        except models.Command.DoesNotExist:
            raise Http404

    def get(self, request, pk, food_id, value, format=None):

        client = self.get_object(pk)
        food = models.DefaultCommand.objects.get(id=food_id)
        if value:
            client.client_command.add(food)
        else:
            client.client_command.remove(food)

        return Response()

class CommandDefaultFoodUpdate(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return models.Command.objects.get(pk=pk)
        except models.Command.DoesNotExist:
            raise Http404

    def get(self, request, pk, food_id, value, format=None):

        command = self.get_object(pk)
        food = models.DefaultCommand.objects.get(id=food_id)
        if value:
            command.meals.add(food)
        else:
            command.meals.remove(food)

        return Response()