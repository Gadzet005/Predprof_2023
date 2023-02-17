import socket
import re

import grequests
from pythonping import ping

from queries.models import SiteQueryNote


class SiteQueryManager(object):
    def __init__(self, sites):
        self.sites = sites

    def _get_status_code(self):
        requests = (grequests.get(site.url) for site in self.sites)
        responses = grequests.map(requests)

        for idx, site in enumerate(self.sites):
            try:
                site.status_code = responses[idx].status_code
            except AttributeError:
                site.status_code = 404

    def _get_ping(self):
        for site in self.sites:
            domen_match = re.search(r'https?://([A-Za-z_0-9.-]+).*', site.url)
            if domen_match:
                domen = domen_match.group(1)
                site.ping = self.get_ping(domen)
            else:
                site.ping = None

    def get_sites_info(self):
        self._get_status_code()
        self._get_ping()

        return self.sites

    def save(self):
        for site in self.sites:
            if site.ping:
                SiteQueryNote.objects.create(
                    site=site, status_code=site.status_code, ping=site.ping
                    )

    @staticmethod
    def get_ping(domen):
        try:
            r = ping(socket.gethostbyname(domen))
            if r.rtt_avg_ms >= 2000:
                return None
            return r.rtt_avg_ms
        except:
            return None
