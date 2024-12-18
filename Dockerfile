FROM python:3.11-alpine

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение в контейнер
COPY ./app /app

ENV FLASK_APP=__init__.py

# Открываем порт для Flask приложения
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0"]

