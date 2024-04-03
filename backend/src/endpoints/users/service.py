from sqlalchemy import select

from src.core.db import get_session
from src.endpoints.users.schemas import UserLogin
from src.models import User


class UserService:
    async def get_user_by_id(self, user_id: int) -> User:
        session = await get_session()
        user = await session.execute(select(User).where(user_id=user_id))
        return user

    async def login_user(self, user_data: UserLogin) -> User:
        session = await get_session()
        user = await session.execute(
            select(User)
            .where(username=user_data.username, password=user_data.password)
        )
        return user
