from django import template

register = template.Library()

def cut_str(value,arg):
    return value.replace(arg,'')

register.filter('cut_str',cut_str)
