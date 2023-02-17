while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 5
done

celery -A config worker -l info