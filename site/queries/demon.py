from queries.request import bd, url_to_status, get_urls
from time import sleep
from django.utils import timezone


def demon():
    while True:
        urls = get_urls()
        urls = url_to_status(urls)
        if urls != None:
            bd(urls)
            print('log time:', timezone.now())
        sleep(60)
