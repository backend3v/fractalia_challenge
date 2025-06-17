from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from models.tasks import TaskDB, Task, TaskUpdate
from utils.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/tasks", response_model=List[Task])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskDB).all()
    return tasks


@router.post("/tasks", response_model=Task)
def create_task(task: Task, db: Session = Depends(get_db)):
    db_task = TaskDB(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task



@router.put("/tasks/{task_id}", response_model=TaskUpdate)
def update_task(task_id: int, task_update: Task, db: Session = Depends(get_db)):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed
    db.commit()
    db.refresh(task)
    return task



@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}