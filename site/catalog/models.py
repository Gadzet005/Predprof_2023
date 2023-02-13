from django.db import models


class Site(models.Model):
    name = models.CharField('название', max_length=100)
    url = models.URLField('url', max_length=100)
    logo = models.ImageField('логотип', upload_to='logo/%Y/%m/', null=True, blank=True)
    description = models.TextField('описание', default='Без описания', max_length=5000)
    is_on_catalog = models.BooleanField('в общем каталоге?', default=False)

    class Meta:
        verbose_name = 'сайт'
        verbose_name_plural = 'сайты'

    def __str__(self):
        return self.name
