from pydantic import BaseModel

from caldav_client.schemas import CalDavInfo


class Person(BaseModel):
    last_name: str
    first_name: str
    middle_name: str | None = None
    email: str


class InviteCode(BaseModel):
    person: Person
    caldav_info: CalDavInfo
