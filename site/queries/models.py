from django.db import models
from catalog.models import Site


class Site_statistics(models.Model):
    id_site = models.ForeignKey(Site, verbose_name='id сайта', on_delete=models.DO_NOTHING, null=True, default='norm')
    status_code = models.IntegerField(verbose_name='статус код')
    ping = models.IntegerField(verbose_name='задержка запроса в миллисекундах')
    note_time = models.DateTimeField(verbose_name='время записи', null=True)
