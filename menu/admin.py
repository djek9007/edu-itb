from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    """Статичные страницы"""
    list_display = ('tree_actions', 'indented_title', 'slug',)
    list_display_links = ('indented_title',)
    list_editable = ('slug',)
    MPTT_ADMIN_LEVEL_INDENT = 20
    # list_filter = ("published", )
    # search_fields = ("name",)
    prepopulated_fields = {"slug": ("name", )}

    actions = ['unpublish', 'publish']
    # сверху админки показывает сохранить удалить
    save_on_top = True
    # readonly_fields = ("slug",)
