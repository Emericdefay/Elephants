from django import template
import random
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