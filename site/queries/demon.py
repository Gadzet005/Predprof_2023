import re
from queries.request import SiteQueryManager
from queries.models import SiteFallReason
from catalog.models import Site
from datetime import datetime
from common.utils import notify_users


def down(site):
    sites = SiteFallReason.objects.all()
    if len(sites) == 0:
        reason = f'Наш сервер обнаружил, что сайт {site.url}'
        SiteFallReason.objects.create(site=site, reason=reason)
        notify_users(site.url, site.status_code, reason)
        return 'fall'
    for FallSite in sites:
        if site.url == FallSite.site.url:
            return None
        reason = f'Наш сервер обнаружил, что сайт {site.url}'
        SiteFallReason.objects.create(site=site, reason=reason)
        notify_users(site.url, site.status_code, reason)
        return 'fall'


def up(site):
    sites = SiteFallReason.objects.all()
    for FallSite in sites:
        if site.url == FallSite.site.url:
            FallSite.delete()
            reason = f'Наш сервер обнаружил, что сайт {site.site.url}'
            notify_users(site.site.url, site.status_code, reason)


def demon():
    start_time = datetime.now()
    print("START PROCESS")

    sites = Site.objects.all()
    manager = SiteQueryManager(sites)
    sites = manager.get_sites_info()
    for site in sites:
        print(site.name, site.url, site.status_code, site.ping, sep='\t')
    manager.save()
    print(SiteFallReason.objects.all())
    for site in sites:
        if site.ping == 2000:
            print(down(site))
        else:
            up(site)

    finish_time = datetime.now()
    print("FINISH PROCESS")
    print('DURATION:', finish_time - start_time)
