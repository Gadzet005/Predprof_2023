#!/bin/sh
while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 5
done
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000

