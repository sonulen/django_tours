from django import template

register = template.Library()


@register.filter
def is_current_page(request, acronym) -> bool:
    return acronym in request.path


@register.filter
def min_by_key(dict_with_data, key: str) -> int:
    # Сгенерируем список только из элементов слова по ключу key
    items_list = [item[1][key] for item in dict_with_data.items()]
    return min(items_list)


@register.filter
def max_by_key(dict_with_data, key: str) -> int:
    # Сгенерируем список только из элементов слова по ключу key
    items_list = [item[1][key] for item in dict_with_data.items()]
    return max(items_list)
