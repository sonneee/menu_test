from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Ссылка')
    parent_item = models.IntegerField(verbose_name='Пункт-родитель')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
