from enum import Enum
from datetime import datetime
from typing import Optional, Self

from . import tags

from pydantic import BaseModel, Field, model_validator


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
    informed: bool = False

    @model_validator(mode='after')
    def process_informed_tag(self) -> Self:
        if tags.INFORMED in self.tags:
            self.informed = True
            self.tags.remove(tags.INFORMED)
        return self


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    tags: Optional[list[str]] = None
    status: Optional[Status] = None
    priority: Optional[int] = None
    executor: Optional[str] = None
