import site
from django.db import models


class SiteQueryNote(models.Model):
    site = models.ForeignKey('catalog.Site', verbose_name='сайт', on_delete=models.CASCADE)
    status_code = models.SmallIntegerField(verbose_name='статус')
    ping = models.FloatField(verbose_name='задержка мс.', null=True)
    note_time = models.DateTimeField(verbose_name='время записи', auto_now_add=True)

    class Meta:
        default_related_name = 'query_notes'
        ordering = ('-note_time',)

class SiteFallReason(models.Model):
    site=models.ForeignKey(Site, verbose_name='сайт', on_delete=models.CASCADE)
    reason=models.TextField(max_length=100, verbose_name='причина падения')
    time=models.DateTimeField(verbose_name='время записи', auto_now_add=True)


