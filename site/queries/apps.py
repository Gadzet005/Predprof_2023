from django.apps import AppConfig
from gevent import monkey


monkey.patch_all()

class QueriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'queries'

    def ready(self):
        from queries.tasks import demon_task
        #demon_task.apply_async()
