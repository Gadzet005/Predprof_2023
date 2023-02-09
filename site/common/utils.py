from django.core.mail import send_mass_mail

import site


def state_change_send_email(site_name, cur_code, recipients_list):
    emails = []
    theme = f'Сайт {site_name} изменил свое состояние'
    if cur_code < 400:
        for recipient in recipients_list:
            message = f'Ресурс {site_name} сейчас доступен'
            emails.append((theme, message, site.config.settings.EMAIL_HOST_USER, [recipient]))
    else:
        for recipient in recipients_list:
            message = f'Ресурс {site_name} сейчас не доступен'
            emails.append((theme, message, site.config.settings.EMAIL_HOST_USER, [recipient]))
    send_mass_mail(emails, fail_silently=False)


