import environ
from config.celery import app as celery_app


__all__ = ('celery_app',)

env = environ.Env()
environ.Env.read_env()
state = env.str('STATE', default='DEV')
if state == 'PROD':
    from .base import *
    from .prod import *
else:
    from .base import *
