from fastapi import FastAPI
from database import engine
import models
from routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task API", description="API REST de gestión de tareas")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task API funcionando"}