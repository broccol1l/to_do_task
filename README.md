# FastAPI To-Do App
Простое CRUD-приложение на FastAPI с использованием асинхронного SQLAlchemy и Docker.

🚀 Как запустить проект
1. Клонируй репозиторий
```bash
git clone https://github.com/broccol1l/to_do_task
```
2. Собери Docker-образ (При ошибке откройте Docker Desktop и введите команду снова)
```bash
docker build -t to_do .
```
3. Запусти контейнер
```bash
docker run -d -p 8000:8000 --name to_do_app to_do
```
Теперь приложение доступно по адресу:

```bash
http://localhost:8000
```
Swagger-документация:
```bash
http://localhost:8000/docs
```
Используемые технологии
FastAPI — фреймворк для создания API

SQLAlchemy (async) — ORM

SQLite — база данных (по умолчанию, можно заменить)

Docker — контейнеризация
