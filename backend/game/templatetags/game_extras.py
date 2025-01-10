from django import template
register = template.Library()

@register.filter
def pairs(lst):
    return zip(lst[::2], lst[1::2])