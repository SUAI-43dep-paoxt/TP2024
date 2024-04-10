from pydantic import BaseModel


class CalDavInfo(BaseModel):
    username: str
    password: str
    url: str
    calendar_name: str
