# Task API
API REST para gestión de tareas desarrollada con Python, FastAPI y SQLite.

## Tecnologías
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite

## Cómo correrlo
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload

## Endpoints
- POST /tasks — Crear tarea
- GET /tasks — Listar tareas
- GET /tasks/{id} — Ver tarea
- PUT /tasks/{id} — Actualizar tarea
- DELETE /tasks/{id} — Eliminar tarea