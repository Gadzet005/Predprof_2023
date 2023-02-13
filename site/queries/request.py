import socket

import grequests
from pythonping import ping

from catalog.models import Site
from queries.models import SiteQueryNote


def request_list(urls):
    objects = (grequests.get(u) for u in urls)
    objects = grequests.map(objects)
    return objects


def mping(url):
    r = ping(socket.gethostbyname(url))
    if r.rtt_avg_ms >= 2000:
        return "Fall"
    return r.rtt_avg_ms


def pings(urls):
    arr = []
    for i in urls:
        if i[5] == "/":
            url = i[7:]
        else:
            url = i[8:]
        arr.append(mping(url))
    return arr


def url_to_status(urls):
    reqs = request_list(urls)
    lpings = pings(urls)
    status_list = []
    for i in range(len(lpings)):
        arr = []
        arr.append(lpings[i])
        arr.append(reqs[i])
        status_list.append(arr)
    return status_list


def get_urls():
    sites = list(Site.objects.all())
    if len(sites) == 0:
        return None
    urls = []
    url_id = []
    for site in sites:
        urls.append(site.url)
        url_id.append(site)
    return urls, url_id


def bd(arr, urls_id):
    for i in range(len(arr)):
        SiteQueryNote.objects.create(
            site=urls_id[i], status_code=int(arr[i][1].status_code),
            ping=arr[i][0]
            )
