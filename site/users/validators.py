from datetime import date

from django.core.exceptions import ValidationError


def birthday_date_validator(birthday_date):
    if birthday_date >= date.today():
        raise ValidationError('Укажите правильную дату рождения')
