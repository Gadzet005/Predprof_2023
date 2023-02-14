from config.celery import app
from queries.demon import demon


@app.task
def demon_task():
    demon()