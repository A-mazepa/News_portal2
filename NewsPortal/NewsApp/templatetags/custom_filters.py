from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value):
    """
    value: значение, к которому нужно применить фильтр
    """
    # Возвращаемое функцией значение подставится в шаблон.
    return f'{value} Р'

words = ['редиска', 'какашка']

@register.filter()
def censor(value):
    for word in words:
        value = value.replace(word, '***')
    return value
