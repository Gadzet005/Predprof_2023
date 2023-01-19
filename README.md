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
- Зайдите в него, **для Windows**
  ```
  venv\Scripts\activate
  ```
- Для **Linux/Mac**
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
- Вы можете создать файл .env в папке config и определить переменные окружения. Пример такого файла - .env-example (в той же папке)
