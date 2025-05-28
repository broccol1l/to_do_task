from database.engine import async_session_maker
from models.models import Task
from datetime import datetime

from sqlalchemy.sql import func

from sqlalchemy import select


async def add_task(title: str, description: str | None, is_completed: bool):
    async with async_session_maker() as session:
        task = Task(title=title,
                    description=description,
                    is_completed=is_completed,
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                    )
        session.add(task)
        await session.commit()
        return task

async def get_all_tasks():
    async with async_session_maker() as session:
        result = await session.execute(select(Task))
        tasks = result.scalars().all()
        return tasks

async def get_task_by_id(task_id: int):
    async with async_session_maker() as session:
        result = await session.execute(select(Task).where(Task.id == task_id))
        task = result.scalar_one_or_none()
        return task

async def update_task(task_id: int, new_title: str | None = None, new_description: str | None = None,
                      is_completed_upd: bool | None = None):
    async with async_session_maker() as session:
        result = await session.execute(select(Task).where(Task.id == task_id))
        task = result.scalar_one_or_none()

        if task is None:
            return None

        if new_title is not None:
            task.title = new_title
        if new_description is not None:
            task.description = new_description
        if is_completed_upd is not None:
            task.is_completed = is_completed_upd

        task.updated_at = func.now()

        await session.commit()
        await session.refresh(task)

        return task


async def delete_task(task_id: int):
    async with async_session_maker() as session:
        result = await session.execute(select(Task).where(Task.id == task_id))
        task = result.scalar_one_or_none()

        if task is None:
            return None

        await session.delete(task)
        await session.commit()
        return "Task is deleted"