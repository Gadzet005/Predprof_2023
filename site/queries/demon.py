from queries.request import SiteQueryManager
from catalog.models import Site


def demon():
    sites = Site.objects.all()
    manager = SiteQueryManager(sites)
    sites = manager.get_sites_info()
    manager.save()
