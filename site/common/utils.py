from django.core.mail import send_mass_mail
from requests import get

from users.models import User
from config.settings import EMAIL_HOST_USER, TELEGRAM_TOKEN


def state_change_send_email(site_name, cur_code, recipients_list):
    emails = []
    theme = f'Сайт {site_name} изменил свое состояние'
    if cur_code < 400:
        message = f'Ресурс {site_name} сейчас доступен'
        for recipient in recipients_list:
            emails.append((theme, message, EMAIL_HOST_USER, [recipient]))
    else:
        message = f'Ресурс {site_name} сейчас не доступен'
        for recipient in recipients_list:
            emails.append((theme, message, EMAIL_HOST_USER, [recipient]))
    send_mass_mail(emails, fail_silently=False)


async def task(site_name, cur_code, recipients_list):
    if cur_code < 400:
        message = f'Ресурс {site_name} сейчас доступен'
        for recipient in recipients_list:
            chat_id = User.objects.get(email=recipient).chat_id
            _ = get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}')

    else:
        message = f'Ресурс {site_name} сейчас не доступен'
        for recipient in recipients_list:
            chat_id = User.objects.get(email=recipient).chat_id
            _ = get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}')

