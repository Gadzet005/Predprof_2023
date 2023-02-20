import re
from queries.request import SiteQueryManager
from time import sleep
from datetime import datetime

from catalog.models import Site
from queries.models import SiteFallReason

def down(site):
    sites=SiteFallReason.objects.all()
    for FallSites in sites:
        if site.url == FallSites.site.url:
            return None
        st="this site fall "+ site.url
        return st

def demon():
    start_time = datetime.now()
    print("START PROCESS")

    sites = Site.objects.all()
    manager = SiteQueryManager(sites)
    sites = manager.get_sites_info()
    for site in sites:
        print(site.name, site.url, site.status_code, site.ping, sep='\t')
    manager.save()
    for site in sites:
        if site.ping==None:
            print(down(site))

    finish_time = datetime.now()
    print("FINISH PROCESS")
    print('DURATION:', finish_time - start_time)

