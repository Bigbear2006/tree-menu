from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu: Menu | str):
    if isinstance(menu, str):
        menu = Menu.objects.get(title=menu)
    return {'menu': menu}
