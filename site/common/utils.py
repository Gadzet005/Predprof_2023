from django.core.mail import send_mass_mail
from requests import get
from users.models import User
from config.settings import EMAIL_HOST_USER, TELEGRAM_TOKEN, EMAIL_HOST_PASSWORD
from send_mail import send_mail


def state_change_send_email(site_name, cur_code, recipients_list, text, state):
    theme = f'Сайт {site_name} изменил свое состояние'

    if state:
        text = f'Ресурс {site_name} сейчас доступен'
        for recipient in recipients_list:
            message = f'Subject: {theme}\n\n{text}'
            send_mail(message)
    else:
        text = f'Ресурс {site_name} сейчас не доступен' + '\n' + text
        for recipient in recipients_list:
            message = f'Subject: {theme}\n\n{text}'
            send_mail(message)


def state_change_send_telegram_notification(site_name, cur_code, recipients_list, text, state):
    print(site_name, cur_code, recipients_list, text)
    if state:
        message = f'Ресурс {site_name} сейчас доступен'
        for recipient in recipients_list:
            chat_id = User.objects.get(email=recipient).chat_id
            if chat_id != 0:
                _ = get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}')

    else:
        message = f'Ресурс {site_name} сейчас не доступен' + '\n' + text
        for recipient in recipients_list:
            chat_id = User.objects.get(email=recipient).chat_id
            if chat_id != 0:
                _ = get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}')

def notify_users(url, status_code, text, state):
    emails = []
    users = User.objects.all()#change on not all users
    for user in users:
        emails.append(user.email)
    state_change_send_email(url, status_code, emails, text, state)
    state_change_send_telegram_notification(url, status_code, emails, text, state)
