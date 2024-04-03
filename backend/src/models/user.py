from sqlmodel import Field, Relationship, SQLModel
from typing_extensions import TYPE_CHECKING

from src.models.role import Role

if TYPE_CHECKING:
    from src.models.team import Team


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int = Field(primary_key=True, nullable=False)
    first_name: str
    last_name: str
    middle_name: str
    username: str
    password: str

    teams: list["Team"] = Relationship(back_populates="users", link_model=Role)
