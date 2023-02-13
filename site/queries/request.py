import socket
import re

import grequests
from pythonping import ping

from queries.models import SiteQueryNote


def get_sites_status_code(sites):
    requests = (grequests.get(site.url) for site in sites)
    responses = grequests.map(requests)
    for idx, site in enumerate(sites):
        site.status_code = responses[idx].status_code
    return sites


def get_site_ping_by_domen(domen):
    r = ping(socket.gethostbyname(domen))
    if r.rtt_avg_ms >= 2000:
        return 'Fall'
    return r.rtt_avg_ms


def get_sites_ping(sites):
    def _get_sites_ping():
        for site in sites:
            domen_match = re.search(r'https?://([A-Za-z_0-9.-]+).*', site.url)
            if domen_match:
                domen = domen_match.group(1)
                site.ping = get_site_ping_by_domen(domen)
                yield site

    return list(_get_sites_ping())


def get_sites_info(sites):
    sites = get_sites_status_code(sites)
    sites = get_sites_ping(sites)
    return sites


def save_notes(sites):
    for site in sites:
        SiteQueryNote.objects.create(site=site, status_code=site.status_code, ping=site.ping)
