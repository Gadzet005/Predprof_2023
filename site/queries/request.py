import socket
from pythonping import ping
import grequests
from django.utils import timezone
from queries.models import Site_statistics
from catalog.models import Site


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
    for site in sites:
        urls.append(site.url)
    return urls

def bd(arr):
    for i in arr:
        note = Site_statistics()
        create_note(note, int(i[1].status_code), i[0])


def create_note(note, status_code, ping, url=None):
    note.status_code = status_code
    note.ping = ping
    note.note_time = timezone.now()
    note.save()
if __name__ == '__main__':
    print(pings(['https://google.com']))