from django import template
from django.utils import timezone


register = template.Library()


@register.simple_tag()
def get_site_status(site):
    last_query_note = site.query_notes.first()
    if not last_query_note:
        return None
    
    ping = last_query_note.ping
    status_code = last_query_note.status_code

    return {
        'ping': ping, 'status_code': status_code
        }
