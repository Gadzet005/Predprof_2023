# Команда **"Тонущий корабль"**

![Python test](https://github.com/Gadzet005/Predprof_2023/actions/workflows/python.yml/badge.svg)
![Django test](https://github.com/Gadzet005/Predprof_2023/actions/workflows/django.yml/badge.svg)

## Инструкция по установке
- Загрузите проект

  ```
  git clone https://github.com/Gadzet005/Predprof_2023
  ```
  
- Перейдите в в папку проекта

- Переименуйте .env-example в .env

### Продакшн
**Для запуска в режиме продашн у вас должен быть установлен docker**
- Поменяйте в .env файле параметр STATE на PROD и подставьте в параметр TELEGRAM_TOKEN ваш токен
- Если у вас Windows, то пропишите ``` git config --global core.autocrlf false ```
- Запустите докер

  ```
  docker-compose build
  docker-compose up
  ```
Сайт будет доступен по адресу localhost

### Разработка
**В режиме разработки телеграм бот и система по отслеживанию работы сайтов не будут автоматически запущены**

- Создайте виртуальное окружение

  ```
  python -m venv venv
  ```

- Зайдите в него

  - Windows
  ```venv/Scripts/activate```
  - Linux/Mac
  ```source venv/bin/activate```

- Загрузите внешние зависимости

  ```
  pip install -r requirements.txt
  ```
 
- Примените миграции

  ```
  python site/manage.py migrate
  ```
 
- Запустите проект

  ```
  python site/manage.py runserver
  ```

## Настройка
- Настроить проект можно с помощью .env файла в корне проекта (см. .env-example)
