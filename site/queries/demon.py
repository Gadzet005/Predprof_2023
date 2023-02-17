from queries.request import SiteQueryManager
from datetime import datetime
from catalog.models import Site


def demon():
    start_time = datetime.now()
    print('START PROCESS')

    sites = Site.objects.all()
    try:
        manager = SiteQueryManager(sites)
        sites = manager.get_sites_info()
        for site in sites:
            print(site.name, site.url, site.status_code, site.ping, sep='\t')
        manager.save()
    except Exception:
        print('ERROR')

    finish_time = datetime.now()
    print('FINISH PROCESS')
    print('DURATION:', finish_time - start_time)
