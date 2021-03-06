from django import template
import random
import locale
from ..models import Food, Client, Circuit, Command, DefaultCommand, FoodCategory, WeekRange
from django.db.models import Q, Sum, Prefetch, F, Avg, Case, When, Value
from django.db.models import FloatField
from decimal import Decimal
from django.db.models.functions import Round
from django.utils.translation import gettext as _
from datetime import timedelta, datetime
import isoweek
from dateutil.relativedelta import relativedelta
import datetime as datetime_
import numpy as np
from colormap import rgb2hex, rgb2hls, hls2rgb

register = template.Library()

@register.filter
def index1(indexable, i):
    return indexable[i-1]

@register.filter
def tofloat(str_nbr):
    if str_nbr:
        return str(str_nbr).replace(',', '.')
    else:
        return 0

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def to_int(obj):
    return int(obj)

@register.filter
def firsts(indexable, i):
    return indexable[:i]

@register.filter
def nonpadded(string):
    if string[0] == '0':
        return string[1:]
    return string

@register.filter
def padded(string):
    if len(string) == 1:
        return f"0{string}"
    return string

@register.filter
def get(obj, key):
    try:
        return (obj[key])
    except IndexError:
        return

@register.filter
def get_futur(obj, key):
    try:
        return (obj[key])
    except IndexError:
        return

@register.filter
def getattr_(obj, key):
    try:
        return getattr(obj, str(key))
    except IndexError:
        return

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value

@register.filter
def list_(obj, a):
    return list(range(a))


@register.filter
def analyse(obj):
    return (obj)

@register.filter
def get_value(obj, key):
    return obj[key]

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))

def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb2hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls2rgb(h, l, s)
    return rgb2hex(int(r * 255), int(g * 255), int(b * 255))

def darken_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 - factor)
    
@register.filter
def get_value_darker(obj):
    r, g, b = hex_to_rgb(obj)

    return darken_color(r,g,b)


@register.filter
def year(obj):
    return obj.year

@register.filter
def month(obj):
    return obj.month

@register.filter
def month_name(obj):
    return _(obj.strftime("%B"))

@register.filter
def day(obj):
    return obj.day

@register.filter
def day_plusone(obj):
    return (obj + relativedelta(days=+1)).day

@register.filter
def year_plusone(obj):
    return (obj + relativedelta(years=+1)).year

@register.filter
def day_plusone_equal_1(obj):
    return (obj + relativedelta(days=+1)).day == 1

@register.filter
def day_plusone_year_equal_1(obj):
    return (obj + relativedelta(days=+1)).year != obj.year

@register.filter
def month_plusone(obj):
    return (obj + relativedelta(months=+1)).month

@register.filter
def day_name(obj):
    return _(obj.strftime("%A"))

@register.filter
def get_week(obj):
    return obj.isocalendar()[1]

@register.filter
def get_year(obj):
    return obj.isocalendar()[0]


@register.filter
def convert_day_ymd(obj):
    return obj.strftime("%d-%m-%Y")

@register.filter
def convert_day_ymd_plus_one(obj):
    return (obj + relativedelta(days=+1)).strftime("%d-%m-%Y")


@register.filter
def max_week(obj):
    return isoweek.Week.last_week_of_year(obj).week

@register.filter
def test(obj):
    return obj[0]

@register.filter
def make_query(obj):
    try:
        return obj.__class__.objects.all()
    except AttributeError:
        return obj

@register.filter
def make_query_all(obj):
    return Command.objects.filter(id__in={instance.id for instance in obj})

@register.filter
def query_filter_day_date_command(obj, f):
    return obj.filter(day_date_command=f)

@register.filter
def query_filter_day_date_command__in(obj, f):
    return obj.filter(day_date_command__in=f)

@register.filter
def query_filter_month_date_command(obj, f):
    return obj.filter(month_date_command=f)

@register.filter
def query_filter_month_date_command__in(obj, f):
    return obj.filter(month_date_command__in=f)

@register.filter
def query_filter_year_date_command(obj, f):
    return obj.filter(year_date_command=f)

@register.filter
def query_filter_year_date_command__in(obj, f):
    return obj.filter(year_date_command__in=f)

@register.filter
def query_filter_client__circuit(obj, f):
    return obj.filter(client__circuit_id=f)

@register.filter
def query_filter_client_id(obj, f):
    return obj.filter(client__id=f)

@register.filter
def query_filter_search(obj, search):
    try:
        dayone, daytwo = search.split(',')[0], search.split(',')[1]
        qs = obj.filter(
            command_command__gt=0,
            day_date_command__in=[dayone.split('-')[0]],
            month_date_command=dayone.split('-')[1],
            year_date_command=dayone.split('-')[-1],
            ).order_by('client__order')
        qs |= obj.filter(
            command_command__gt=0,
            day_date_command__in=[daytwo.split('-')[0]],
            month_date_command=daytwo.split('-')[1],
            year_date_command=daytwo.split('-')[-1],
            ).order_by('client__order')
        return qs

    except IndexError:
        dayone = search
        obj = obj.filter(
            command_command__gt=0,
            day_date_command__in=[dayone.split('-')[0]],
            month_date_command=dayone.split('-')[1],
            year_date_command=dayone.split('-')[-1],
            ).order_by('client__order')
    return obj

@register.filter
def query_filter_command_passed(obj):
    return obj.filter(command_command__gt=0)

@register.filter
def query_command_id(obj, id_):
    try:
        return obj.filter(id=id_)
    except ValueError:
        return obj

@register.filter
def make_unit_price(obj):
    return Food.objects.filter(id__in=obj.all().values_list('default', flat=True)).aggregate(sum=Round(Sum(F('price')), 2))['sum']

@register.filter
def query_from_id_get_name(obj, id_):
    return Food.objects.get(pk=obj.get(id=id_).pk).category

@register.filter
def query_from_id_get_default_id(obj, id_):
    return Food.objects.get(pk=obj.get(id=id_).pk).pk

@register.filter
def query_from_id_get_price(obj, id_):
    return (Food.objects.get(pk=obj.get(id=id_).pk).price)

@register.filter
def query_food_id(obj, n):
    return obj.get(default=n).pk

@register.filter
def query_command_food(obj, f):
    return obj.filter(meals=f).count()

@register.filter
def query_id(obj, i):
    return obj.filter(client__id=i)

@register.filter
def query_count(obj):
    return obj.count()

@register.filter
def len_list(obj):
    if len(obj) > 1:
        return True
    else:
        return False

@register.filter
def make_unit_price_from_command(obj):
    unit_price = Food.objects.filter(id__in=obj.all().values_list('meals', flat=True)).aggregate(sum=Round(Sum(F('price')), 2))['sum']
    return unit_price if unit_price else 0


@register.filter
def query_sum_meals_this_month(obj):
    meals = obj.aggregate(sum=Sum(F('command_command')))['sum']
    return meals if meals else 0

@register.filter
def query_sum_price_this_month(obj):
    prices = obj.aggregate(sum=Round(
                                Sum(
                                    (F('meals__default__price')) * F('command_command'),
                                    output_field=FloatField(),
                                    )
                                ,2)
                       )['sum']
    return prices if prices else 0

@register.filter
def no_difference(obj):
    price = query_sum_price_this_month(obj)
    meals = query_sum_meals_this_month(obj)
    unit_price = make_unit_price_from_command(obj)
    return unit_price * meals == price

@register.filter
def query_sum_morning(obj, f):

    clients_per_circuit = obj.prefetch_related().all()
    if clients_per_circuit :
        sum_food = 0
        for client in clients_per_circuit:
            sum_food += client.command_command*DefaultCommand.objects.filter(meals__id=client.id).filter(default=f).count()
        return sum_food
    else:
        return 0

@register.filter
def sort_order(lst):
    #from operator import attrgetter
    #lst.sort(key = attrgetter('order'), reverse = True)
    #lst.sort(key=lambda x: x.order, reverse=True)
    custom_list = [rec.id for rec in lst]
    queryset = Client.objects.filter(id__in=custom_list).order_by('order')
    return queryset

@register.filter
def sort_order_c(lst):
    #from operator import attrgetter
    #lst.sort(key = attrgetter('order'), reverse = True)
    #lst.sort(key=lambda x: x.order, reverse=True)
    custom_list = [rec.id for rec in lst]
    queryset = Circuit.objects.filter(id__in=custom_list).order_by('order_c')
    return queryset
