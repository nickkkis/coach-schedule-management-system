# Django (DRF) Backend для Управления Расписанием Фитнес-Тренеров

Проект представляет собой бэкенд приложения для управления расписанием фитнес-тренеров с использованием Django Rest Framework (DRF) и базы данных PostgreSQL.
![image](https://github.com/nickkkis/coach-schedule-management-system/assets/101864581/c2c9c6e9-23f3-4275-8464-fa92e485350a){:height="400px" width="400px"}
![image](https://github.com/nickkkis/coach-schedule-management-system/assets/101864581/840a1b9d-6936-4330-a882-5bcab80e2b5b){:height="400px" width="400px"}
![image](https://github.com/nickkkis/coach-schedule-management-system/assets/101864581/e4a70b33-e04a-4803-87b0-084fe162f307){:height="400px" width="400px"}




## Установка и Запуск

1. **Клонировать репозиторий:**
    ```bash
    git clone https://github.com/nickkkis/coach-schedule-management-system.git
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

    Загрузите фикстуры: Выполните команду loaddata для загрузки фикстур в базу данных

6. **Запустить сервер:**
    ```bash
    python manage.py runserver
    ```

Теперь ваш бэкенд запущен и доступен по адресу http://127.0.0.1:8000/.

## Использование

Вы можете использовать API для управления расписанием фитнес-тренеров согласно [документации API](https://github.com/nickkkis/coach-schedule-management-system/tree/master/Documentation).

