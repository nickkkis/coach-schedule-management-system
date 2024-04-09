# Django (DRF) Backend для Управления Расписанием Фитнес-Тренеров

Проект представляет собой бэкенд приложения для управления расписанием фитнес-тренеров с использованием Django Rest Framework (DRF) и базы данных PostgreSQL.

## Установка и Запуск

1. **Клонировать репозиторий:**
    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. **Перейти в каталог проекта:**
    ```bash
    cd your_project_directory
    ```

3. **Установить зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Настроить базу данных:**
   В файле `settings.py` настройте параметры базы данных PostgreSQL:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Применить миграции:**
    ```bash
    python manage.py migrate
    ```

6. **Запустить сервер:**
    ```bash
    python manage.py runserver
    ```

Теперь ваш бэкенд запущен и доступен по адресу http://127.0.0.1:8000/.

## Использование

Вы можете использовать API для управления расписанием фитнес-тренеров согласно [документации API](link_to_api_docs).

