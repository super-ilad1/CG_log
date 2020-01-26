from django import template
from django.template.defaultfilters import stringfilter
import chardet
register = template.Library()

@register.filter
@stringfilter
def process(value):
    return value.encode('utf-8').decode('unicode_escape')[1:-1]



