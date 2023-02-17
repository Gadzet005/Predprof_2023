from django.db import models

from users.models import User
from catalog.models import Site


class SiteReport(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, verbose_name='сайт', on_delete=models.CASCADE)
    region = models.CharField('регион', max_length=150)
    problem = models.TextField('проблема', max_length=2000)
    creation_datetime = models.DateTimeField(verbose_name='дата и время создания', auto_now_add=True)
    is_checked = models.BooleanField('рассмотрено', default=False)

    class Meta:
        verbose_name = 'сообщение о проблеме'
        verbose_name_plural = 'сообщения о проблеме'

    def __str__(self):
        return f'Сообщение о проблеме от {self.user}'
