# -*- coding: utf-8 -*-
import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.utils import timezone

from dynamic_filenames import FilePattern

page_file_item = FilePattern(
    filename_pattern='{app_label:.25}/{model_name:.30}/{uuid:base32}{ext}'
)
class Pages(models.Model):
    """Страницы"""
    title = models.CharField(_("Атауы"), max_length=250)
    slug = models.SlugField("Сілтеме", max_length=50, unique=True)
    image = models.ImageField("фотография", upload_to=page_file_item, blank=True, null=True)
    text = RichTextUploadingField(_('Cипаттамасы'))
    published_date = models.DateTimeField(_("Жарияланған күні"), blank=True, null=True, default=timezone.now,)
    published = models.BooleanField(_("Көрсету?"), default=True)

    def __unicode__(self):
        return self.title
    #
    # def get_absolute_url(self):
    #     return reverse('pages:page-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Бет"
        verbose_name_plural = "Беттер"
