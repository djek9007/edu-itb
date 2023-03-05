# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    """Класс модели категорий сетей"""
    name = models.CharField("Атауы", max_length=100)
    slug = models.CharField("url", max_length=50, unique=True, blank=True, null=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Жоғарғы меню",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    published = models.BooleanField("Көрсету", default=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Меню"
        verbose_name_plural = "Меню"
