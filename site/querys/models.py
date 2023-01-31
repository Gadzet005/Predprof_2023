from django.db import models


class Urls(models.Model):
    url = models.TextField()
    status_code = models.IntegerField()
    ping = models.TimeField()
    time = models.DateTimeField()

    def __str__(self):
        return 'id query: ' + str(url)
    
