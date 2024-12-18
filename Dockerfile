FROM python:3.11-alpine

WORKDIR /app

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение в контейнер
COPY ./app /app

ENV FLASK_APP=__init__.py

EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0"]

