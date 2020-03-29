from django import template
from django.urls import resolve

register = template.Library()

@register.filter
def is_current_page(request, acronym) -> bool:
    return acronym in request.path

@register.filter
def min_by_key(dict, key: str) -> int:
    # Сгенерируем список только из элементов слова по ключу key
    list_ = [item[1][key] for item in dict.items()]
    return min(list_) 

@register.filter
def max_by_key(dict, key: str) -> int:
    # Сгенерируем список только из элементов слова по ключу key
    list_ = [item[1][key] for item in dict.items()]
    return max(list_) 