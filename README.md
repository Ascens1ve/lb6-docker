# Лабораторная работа №6
В работе используется легковесное веб-приложение, разработанное на Python с использованием Flask и PostgreSQL.
Приложение организовано с использованием Docker и Docker Compose.

Используются только легковесные образы: python:3.11-alpine и postgres:alpine.

Конфигурация происходит с переменной окружения DATABASE_URL.

База данных хранится в db_data.

Создание таблиц происходит при старте приложения - автоматические миграции.

Для очистки кеша используется параметр --no-cache-dir при установке зависимостей.

# Структура проекта

```
lb6/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── requirements.txt
|   └── templates/
|        ├── index.html
│        ├── departments.html
|        ├── products.html
|        └── store.html
|   
├── Dockerfile
├── docker-compose.yml
└── .env
```

# Запуск приложения

Команда для сборки и запуска приложения:

```bash
docker-compose up --build
```

Данная команда создает необходимые Docker-образы и запускает контейнеры для Flask приложения и базы данных PostgreSQL.

Проверка осуществляется следующей командой:

```bash
docker ps
```

Полученный результат:
```plaintext
231f19939502   lb6-docker-web    "flask run --host=0.…"   5 seconds ago   Up 4 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   lb6-docker-web-1
6e3562c0a5ed   postgres:alpine   "docker-entrypoint.s…"   5 seconds ago   Up 4 seconds   5432/tcp                                    lb6-docker-db-1
```

Видно, что оба контейнера работают.
