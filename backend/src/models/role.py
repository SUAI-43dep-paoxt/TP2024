from sqlmodel import Field, SQLModel


class Role(SQLModel, table=True):
    __tablename__ = "role"

    user_id: int = Field(foreign_key="user.id", primary_key=True)
    team_id: int = Field(foreign_key="team.id", primary_key=True)
