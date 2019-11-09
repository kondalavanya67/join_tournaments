from django import template
import datetime

register = template.Library()


@register.filter
def filter_date(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return str(date.day) + '-' + str(date.month) + '-' + str(date.year)

