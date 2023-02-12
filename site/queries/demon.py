from queries.request import bd, url_to_status, get_urls
from time import sleep
from django.utils import timezone


def demon():
    while True:
        urls, urls_id = get_urls()
        urls = url_to_status(urls)
        if urls is not None:
            bd(urls, urls_id)
            print('log time:', timezone.now())
        sleep(60)
