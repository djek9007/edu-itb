from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
from dynamic_filenames import FilePattern
from image_cropping import ImageRatioField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


page_file_item = FilePattern(
    filename_pattern='{app_label:.25}/{model_name:.30}/{uuid:base32}{ext}'
)

class Category(MPTTModel):
    """Класс модели категорий сетей"""
    name = models.CharField("Атауы", max_length=100)
    slug = models.CharField("url", max_length=50, unique=True, blank=True, null=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Жоғары санат",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    published = models.BooleanField("Көрсету?", default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_post', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = "Санат"
        verbose_name_plural = "Санат"



class Post(models.Model):
    """Класс модели поста"""
    category = TreeForeignKey(
        Category,
        verbose_name="Санат",
        on_delete=models.CASCADE,
    )
    title = models.CharField("Атауы", max_length=500)
    slug = models.SlugField("url", max_length=50, unique=True)
    text = RichTextUploadingField(_('Cипаттамасы'))
    short= models.CharField(verbose_name='Қысқаша жазбасы', max_length=255)
    created_date = models.DateTimeField("Құрылған күні", auto_now_add=True)
    published_date = models.DateTimeField(
        "Жариялау күні",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField("Басты фотосы", upload_to=page_file_item, help_text='490x337', null=True, blank=True)
    cropping = ImageRatioField('image', '490x337', verbose_name='қысқаша фотосы')
    detail_photo = ImageRatioField('image', '1100x690', verbose_name='Фотоны толығымен көрсету')
    published = models.BooleanField("Көрсету?", default=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail_post', kwargs={'category_slug': self.category.slug, 'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посттар"


class Files(models.Model):
    """Файл тіркемелері"""
    post = models.ForeignKey(Post, verbose_name='Файл тіркемелері', on_delete=models.CASCADE,  related_name='fileitems',)
    file = models.FileField('Файл жүктеуге', upload_to=page_file_item, blank=True, null=True, validators=[FileExtensionValidator(['pdf'])])
    description = models.CharField(verbose_name='Файл атауы', max_length=250, blank=True, null=True)
    published = models.BooleanField("Көрсету?", default=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлдар"

class Comment(models.Model):
    """пікірлер"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост',related_name='comments',)
    author = models.CharField(verbose_name='Есімі', max_length=100)
    email = models.EmailField(verbose_name='Email',max_length=50)
    comment = models.TextField(verbose_name='Пікіріңіз')
    published = models.BooleanField("Көрсету?", default=True)
    created_date = models.DateTimeField("Пікір жазылған күн", auto_now_add=True)

    class Meta:
        verbose_name = "Пікір"
        verbose_name_plural = "Пікірлер"