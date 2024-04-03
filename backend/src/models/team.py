from sqlmodel import Field, Relationship, SQLModel
from typing_extensions import TYPE_CHECKING

from src.models.role import Role

if TYPE_CHECKING:
    from src.models.user import User


class Team(SQLModel, table=True):
    __tablename__ = "team"

    id: int = Field(primary_key=True, nullable=False)
    name: str

    users: list["User"] = Relationship(back_populates="teams", link_model=Role)
