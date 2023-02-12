from django.db import models
from users.models import User

# Create your models here.


class SiteReports(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    url = models.CharField(verbose_name='Адрес сайта', max_length=300)
    region = models.CharField(verbose_name='Регион', max_length=150)
    problem = models.TextField(verbose_name='Проблема', max_length=2000)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'
