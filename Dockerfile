# Используем базовый образ Python
FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем зависимости проекта и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем все содержимое текущей директории внутрь контейнера
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
