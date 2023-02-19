from queries.request import SiteQueryManager
from catalog.models import Site


def demon():
    sites = Site.objects.all()
    manager = SiteQueryManager(sites)
    sites = manager.get_sites_info()
    for site in sites:
        print(site.name, site.url, site.status_code, site.ping)
    manager.save()
