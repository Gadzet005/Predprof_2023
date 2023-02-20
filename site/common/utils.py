from django.core.mail import send_mass_mail
from requests import get
from users.models import User
from config.settings import EMAIL_HOST_USER, TELEGRAM_TOKEN


def state_change_send_email(site_name, cur_code, recipients_list, text, state):
    emails = []
    theme = f'Сайт {site_name} изменил свое состояние'
    if  state:
        message = f'Ресурс {site_name} сейчас доступен'
        for recipient in recipients_list:
            emails.append((theme, message, EMAIL_HOST_USER, [recipient]))
    else:
        message = f'Ресурс {site_name} сейчас не доступен' + '\n' + text
        for recipient in recipients_list:
            emails.append((theme, message, EMAIL_HOST_USER, [recipient]))
    send_mass_mail(emails, fail_silently=False)


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
