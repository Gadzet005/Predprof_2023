from config.celery import app
from queries.demon import demon


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(20.0, demon_task.s(), name='request_demon') 

@app.task()
def demon_task():
    demon()
    return 'demon loop done'