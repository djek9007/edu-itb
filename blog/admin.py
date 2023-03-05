from django.contrib import admin

# Register your models here.
from image_cropping import ImageCroppingMixin

from blog.models import Category, Post, Files, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ('id','name', 'slug', 'published',)
    list_display_links = ('name',)
    list_filter = ("published", )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name", )}
    # сверху админки показывает сохранить удалить
    save_on_top = True
    # readonly_fields = ("slug",)


class FileItemInline(admin.StackedInline):
    model = Files

@admin.register(Post)
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ('id','title', 'slug', 'category', 'published',)
    list_display_links = ('title',)
    list_filter = ('category',"published", )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("title", )}
    inlines = [FileItemInline,]
    # сверху админки показывает сохранить удалить
    save_on_top = True

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'created_date', 'published' )
    list_display_links = ('author',)
