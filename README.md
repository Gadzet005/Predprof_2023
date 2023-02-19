# Команда **"Тонущий корабль"**

![Python test](https://github.com/Gadzet005/Predprof_2023/actions/workflows/python.yml/badge.svg)
![Django test](https://github.com/Gadzet005/Predprof_2023/actions/workflows/django.yml/badge.svg)

## Инструкция по установке
- Загрузите проект
  ```
  git clone https://github.com/Gadzet005/Predprof_2023
  ```
- Перейдите в в папку проекта
  ```
  cd Predprof_2023
  ```
- Создайте виртуальное окружение
  ```
  python -m venv venv
  ```
- Зайдите в venv
-- Windows
  ```
  venv/Scripts/activate
  ```
-- Linux/Mac
  ```
  source venv/bin/activate
  ```
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
