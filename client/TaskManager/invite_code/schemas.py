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


"""
python console - создание инвайт кода
from invite_code.services import *
from invite_code.services import *
from caldav_client.schemas import CalDavInfo
invite_code = InviteCode(person=Person(last_name="test1",
                                       first_name="test2",
                                       middle_name="test3",
                                       email="email"
                                       ),
                         caldav_info=CalDavInfo(username="test1", password="test2", url="sqwee", calendar_name="qweqw"))
get_encrypted_invite_code(invite_code)

"""