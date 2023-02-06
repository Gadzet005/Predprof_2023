from django.db import models
from django.urls import reverse

from users.models import User
from catalog.managers import SiteManager


class Site(models.Model):
    name = models.CharField('название', max_length=100)
    url = models.URLField('url', max_length=100)
    logo = models.ImageField('логотип', upload_to='logo/%Y/%m/', null=True, blank=True)
    description = models.TextField('описание', default='Без описания', max_length=5000)
    is_on_catalog = models.BooleanField('в общем каталоге?', default=False)

    objects = SiteManager()

    class Meta:
        verbose_name = 'сайт'
        verbose_name_plural = 'сайты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:detail', kwargs={'site_id': self.pk})


class UserSite(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, verbose_name='сервис', on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'user_site'
