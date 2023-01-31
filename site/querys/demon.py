#from .models import Urls
import datetime
from django.utils import timezone
from time import sleep
from request import request_list

print('demon working')

urls = [
    'http://www.heroku.com',
    'http://tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]

while True:
    links = request_list(urls)
    for link in links:
        print(link)
    sleep(60)
    