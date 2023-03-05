# -*- coding: utf-8 -*-
from django import template

from blog.models import Post
from menu.models import Menu

register = template.Library()



@register.simple_tag()
def show_menu():
    return Menu.objects.filter(published=True)

@register.simple_tag()
def show_footer_menu():
    return Post.objects.filter(published=True, category='8')