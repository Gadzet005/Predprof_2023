while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 5
done

python3 manage.py telegram_bot