from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from utils.database import Base



class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)



class Task(BaseModel):
    title: str
    description: str = None
    completed: bool = False