from django.contrib import admin

# Register your models here.
from page.models import Pages


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ('title', 'slug', 'published',)
    list_display_links = ('title',)
    list_filter = ("published", )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("title", )}
    # сверху админки показывает сохранить удалить
    save_on_top = True
    # readonly_fields = ("slug",)