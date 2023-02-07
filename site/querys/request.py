import grequests
import datetime
from django.utils import timezone


def request_list(urls):
    objects = (grequests.get(u) for u in urls)
    objects = grequests.map(objects)
    return objects


"""
create_note функция для создания записи в бд
первый аргумент это экземпляр класса бд
пример:
from querys.models import Site_statistics


note = Site_statistics()
create_note(note, 200, 20)

url пока нет т.к надо ещё связующий функционал пилить
незабудь перед любым изминением и первым использованием бд
python manage.py makemigrations
python manage.py migrate

"""
def create_note(note, status_code, ping, url=None):
    note.status_code = status_code
    note.ping = ping
    note.note_time = timezone.now()
    note.save()
