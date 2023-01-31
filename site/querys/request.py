import grequests

def request_list(urls):
    objects = (grequests.get(u) for u in urls)
    objects = grequests.map(objects)
    return objects
