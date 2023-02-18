from queries.request import SiteQueryManager
from datetime import datetime
from catalog.models import Site


def demon():
    start_time = datetime.now()
    print("START DEMON")

    sites = Site.objects.all()
    manager = SiteQueryManager(sites)
    sites = manager.get_sites_info()
    for site in sites:
        print(site.name, site.url, site.status_code, site.ping)
    manager.save()

    finish_time = datetime.now()
    print("FINISH DEMON")
    print('DURATION:', finish_time - start_time)
