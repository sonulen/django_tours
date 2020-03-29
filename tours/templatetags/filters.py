from django import template
from django.urls import resolve

register = template.Library()
@register.filter
def is_current_page(request, acronym):
    return acronym in request.path