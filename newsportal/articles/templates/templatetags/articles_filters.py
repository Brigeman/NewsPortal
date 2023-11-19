from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='censor')
def censor(value):
    # Список нежелательных слов для цензуры
    unwanted_words = ['редиска', 'шлепокмоянезный', 'кринге']

    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))

    return mark_safe(value)