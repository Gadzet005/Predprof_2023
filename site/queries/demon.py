from queries.request import save_notes, get_sites_info
from time import sleep
from django.utils import timezone

from catalog.models import Site


def demon():
    while True:
        sites = Site.objects.all()
        sites = get_sites_info(sites)
        save_notes(sites)

        print('log time:', timezone.now())
        sleep(60)
