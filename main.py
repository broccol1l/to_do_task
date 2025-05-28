from fastapi import FastAPI, HTTPException

from database.task_service import add_task, get_all_tasks, get_task_by_id, update_task, delete_task
from typing import Optional
from database.engine import create_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    print("Database is ready")
    yield
    print("App is turned off")


app = FastAPI(lifespan=lifespan)



@app.get('/')
async def func():
    return {"data": "successful"}


@app.post("/tasks/", summary='Add new task', description="Creates task with title, description and status")
async def add_task_api(title: str, description: Optional[str] = None, is_completed: bool = False):
    return await add_task(title, description, is_completed)

@app.get("/tasks/", summary="Get all tasks")
async def get_all_tasks_api():
    return await get_all_tasks()

@app.get("/tasks/{task_id}", summary="Get task by id", description="Enter id and get exact task")
async def get_task_by_id_api(task_id: int):
    task = await get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return task

@app.put("/tasks/{task_id}", summary="Update task", description="Update every or exact field if needed")
async def update_task_api(task_id: int, new_title: str | None = None, new_description: str | None = None,
                      is_completed_upd: bool | None = None):
    updated_task = await update_task(task_id, new_title, new_description, is_completed_upd)
    if not updated_task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return updated_task


@app.delete("/tasks/{task_id}", summary="Delete task", description="Just delete task by id")
async def delete_task_api(task_id: int):
    deleted_task = await delete_task(task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return {"detail": "Task deleted successfully"}