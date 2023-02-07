from django.db import models
from catalog.models import Site

class Site_statistics(models.Model):
    id_site = models.ForeignKey(Site, verbose_name='id сайта' , on_delete=models.DO_NOTHING, null=True)
    status_code = models.IntegerField(verbose_name='статус код')
    ping = models.TimeField(verbose_name='задержка запроса сайта')
    note_time = models.DateTimeField(verbose_name='время записи', null=True)

    def __str__(self):
        return 'id сайта: '+ str(id_site)
    
