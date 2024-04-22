from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CalDavInfo(BaseModel):
    username: str
    password: str
    url: str
    calendar_name: str


class Status(Enum):
    todo = 'TO DO'
    in_progress = 'IN PROGRESS'
    done = 'DONE'
    cancelled = 'CANCELLED'


class CalDavStatus(Enum):
    needs_action = 'NEEDS-ACTION'
    in_progress = 'IN-PROCESS'
    completed = 'COMPLETED'
    cancelled = 'CANCELLED'


class Task(BaseModel):
    uid: Optional[str] = None
    title: str
    description: str
    create_time: Optional[datetime] = None
    start_time: datetime
    end_time: datetime
    tags: list[str]
    status: Status = Field(default=Status.todo)
    priority: int = Field(default=9, ge=0, lt=10)
    creator: Optional[str] = None
    executor: Optional[str] = None

