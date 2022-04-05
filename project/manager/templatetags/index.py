from django import template
import random
import locale
from ..models import Food, Client, Circuit, Command, DefaultCommand, FoodCategory, WeekRange
from django.db.models import Q, Sum, Prefetch
from django.utils.translation import gettext as _
from datetime import timedelta, datetime
import isoweek
from dateutil.relativedelta import relativedelta
import datetime as datetime_
register = template.Library()

@register.filter
def index1(indexable, i):
    return indexable[i-1]

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def firsts(indexable, i):
    return indexable[:i]

@register.filter
def nonpadded(string):
    if string[0] == '0':
        return string[1:]
    return string

@register.filter
def get(obj, key):
    try:
        return (obj[key])
    except IndexError:
        return

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.filter
def list_(obj, a):
    return list_(range(a))


@register.filter
def analyse(obj):
    print(obj)
    return (obj)

@register.filter
def get_value(obj, key):
    return obj[key]

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
    return obj.__class__.objects.all()

@register.filter
def query_filter_day_date_command(obj, f):
    return obj.filter(day_date_command=f)

@register.filter
def query_filter_month_date_command(obj, f):
    return obj.filter(month_date_command=f)

@register.filter
def query_filter_year_date_command(obj, f):
    return obj.filter(year_date_command=f)

@register.filter
def query_filter_client__circuit(obj, f):
    return obj.filter(client__circuit=f)

@register.filter
def query_filter_command_passed(obj):
    return obj.filter(command_command__gt=0)

@register.filter
def query_count(obj):
    return obj.count()

@register.filter
def query_sum_morning(obj, f):
    a = obj.prefetch_related().all()
    if a :
        return DefaultCommand.objects.filter(meals__id__in=obj.prefetch_related().all()).filter(default=f.category).count()
    else:
        return 0





