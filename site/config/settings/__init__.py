import environ


env = environ.Env()
environ.Env.read_env()
state = env.str('STATE', default='DEV')
if state == 'PROD':
    from .base import * # noqa
    from .prod import * # noqa
else:
    from .base import * # noqa
