from enum import Enum
from datetime import datetime
from pydantic import BaseModel


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
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    tags: list[str]
    status: Status
    creator: str
    executor: str
