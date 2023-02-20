import re
from queries.request import SiteQueryManager
from queries.models import SiteFallReason
from catalog.models import Site
from datetime import datetime
from common.utils import notify_users


def down(site):
    sites = SiteFallReason.objects.all()
    if len(sites) == 0:
        reason = f'по причине статус кода: {site.status_code}'

        if site.ping == 2000:
            reason = 'по причине высокой задержки: больше 2000ms'

        SiteFallReason.objects.create(site=site, reason=reason)
        notify_users(site.url, site.status_code, reason, False)
        return 'fall'

    for FallSite in sites:
        if site.url == FallSite.site.url:
            return None
    reason = f'по причине статус кода: {site.status_code}'
    if site.ping == 2000:
        reason = 'по причине высокой задержки: больше 2000ms'
    SiteFallReason.objects.create(site=site, reason=reason)
    notify_users(site.url, site.status_code, reason, False)
    return 'fall'


def up(site):
    sites = SiteFallReason.objects.all()
    for FallSite in sites:
        if site.url == FallSite.site.url:
            FallSite.delete()
            reason = f'Наш сервер обнаружил, что сайт {site.url} доступен'
            notify_users(site.url, site.status_code, reason, True)


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
        if site.ping == 2000 or site.status_code > 400:
            print(down(site))
        else:
            up(site)

    finish_time = datetime.now()
    print("FINISH PROCESS")
    print('DURATION:', finish_time - start_time)
