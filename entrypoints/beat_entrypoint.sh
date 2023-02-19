while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 5s
done

celery -A config beat -l info