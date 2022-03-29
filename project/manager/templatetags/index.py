from django import template
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