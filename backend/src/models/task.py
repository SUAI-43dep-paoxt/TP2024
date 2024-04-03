from datetime import date

from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    __tablename__ = "task"

    id: int = Field(primary_key=True, nullable=False)
    title: str
    description: str
    status: int
    deadline: date
    implementor_id: int | None = Field(foreign_key="user.id", default=None, primary_key=True)
    team_id: int | None = Field(foreign_key="team.id", default=None, primary_key=True)
