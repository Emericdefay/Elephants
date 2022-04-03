from django import template
import random
import locale
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
    return (obj[key])

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.filter
def list(obj, a):
    return list(range(a))


@register.filter
def analyse(obj):
    return type(obj)

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
    print(obj)
    print((obj + relativedelta(days=+1)).day)
    return (obj + relativedelta(days=+1)).day

@register.filter
def day_name(obj):
    return _(obj.strftime("%A"))

@register.filter
def get_week(obj):
    return obj.isocalendar()[1]

@register.filter
def get_year(obj):
    print(obj)
    print(obj.isocalendar())
    return obj.isocalendar()[0]

# @register.filter
# def get_month(obj):
#     return obj.isocalendar()[2]

@register.filter
def max_week(obj):
    return isoweek.Week.last_week_of_year(obj).week

@register.filter
def test(obj):
    return obj[0]





