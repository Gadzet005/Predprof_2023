import imp
import re
from tabnanny import verbose
import grequests ,socket

from pythonping import ping




def request_list(urls):
    objects = (grequests.get(u) for u in urls)
    objects = grequests.map(objects)
    return objects



def mpnig(url):
    r=ping(socket.gethostbyname(url))
    if r.rtt_avg_ms>=2000:
        return "Fall"
    return r.rtt_avg_ms

def pings(urls):
    arr=[]
    for i in urls:
        if i[5]=="/":
            url=i[7:]
        else:
            url=i[8:]
        arr.append(mpnig(url))
    return arr

def merger(urls):
    reqs=request_list(urls)
    lpings=pings(urls)
    status_list=[]
    for i in range(len(lpings)):
        arr=[]
        arr.append(lpings[i])
        arr.append(reqs[i])
        status_list.append(arr)
    return status_list
        




