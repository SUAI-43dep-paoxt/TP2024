from pydantic import BaseModel, field_validator
from enum import Enum


class CalDavInfo(BaseModel):
    username: str
    password: str
    url: str
    calendar_name: str


class TaskType(Enum):
    vevent = 'VEVENT'
    vtodo = 'VTODO'
    vjournal = 'VJOURNAL'


class Task(BaseModel):
    title: str
    description: str
    start_time: str
    deadline: str
    tags: list[str]
    type: TaskType
    status: str


    @field_validator('status')
    @classmethod
    def validate_status(cls, value, values) -> str:
        type = values['type']
        if type == TaskType.vevent:
            if value == 'TENTATIVE' or value == 'CONFIRMED' or value == 'CANCELLED':
                return value
            else:
                raise ValueError('Invalid status value')
        elif type == TaskType.vtodo:
            if value == 'NEEDS-ACTION' or value == 'COMPLETED' or value == 'IN-PROCESS' or value == 'CANCELLED':
                return value
            else:
                raise ValueError('Invalid status value')
        elif type == TaskType.vjournal:
            if value == 'DRAFT' or value == 'FINAL' or value == 'CANCELLED':
                return value
            else:
                raise ValueError('Invalid status value')
        else:
            raise ValueError('Invalid type value')
