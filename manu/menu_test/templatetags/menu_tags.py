from django import template
import menu_test.views as views

register = template.Library()

@register.simple_tag(takes_context=True)
def get_shops():
    return views.shop