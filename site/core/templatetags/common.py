import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F


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


@register.simple_tag()
def site_query_notes_to_json(site):
    query_notes = list(
        site.query_notes
        .filter(ping__isnull=False)
        .reverse()
        .annotate(
            hour=F('note_time__hour'),
            minute=F('note_time__minute'),
        )
        .values('ping', 'hour', 'minute')
        )

    return json.dumps(query_notes, cls=DjangoJSONEncoder)
