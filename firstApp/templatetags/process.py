from django import template
from django.template.defaultfilters import stringfilter
import re
register = template.Library()

@register.filter
@stringfilter
def process(value):
    return value.encode('utf-8').decode('unicode_escape')[1:-1]

@register.filter
@stringfilter
def fetch_unit(value):
    print("dealing with fetch unit")
    print(value)
    value = re.findall('https://forums.creativecow.net/thread/19/(\d*)', value)


    value = "/post/" + value[0]

    return value


