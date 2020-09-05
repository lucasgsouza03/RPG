from django import template

register = template.Library()

@register.filter(name='positivo')
def positivo(text):
    text = abs(int(text))
    return str(text)