from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import List

from src.core.db import get_session
from src.models import Task


router = APIRouter()


@router.post("/tasks/", response_model=Task)
async def create_task(task: Task, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        db_task = Task.from_orm(task)
        session.add(db_task)
        await session.commit()
        await session.refresh(db_task)
    return db_task


@router.get("/tasks/", response_model=List[Task])
async def get_tasks(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        return (await session.execute(select(Task))).scalars().all()


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        task = await session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(
    task_id: int, task: Task, session: AsyncSession = Depends(get_session)
):
    async with session.begin():
        db_task = await session.get(Task, task_id)
        if not db_task:
            raise HTTPException(status_code=404, detail="Task not found")
        for key, value in task.dict().items():
            setattr(db_task, key, value)
        await session.commit()
        await session.refresh(db_task)
        return db_task


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        task = await session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        await session.delete(task)
        await session.commit()
        return {"message": "Task deleted successfully"}
