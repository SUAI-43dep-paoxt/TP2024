from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from src.core.auth import get_current_user_id
from src.endpoints.users.schemas import UserLogin
from src.endpoints.users.service import UserService

router = APIRouter()


@router.post('/login')
async def login(
    user_login: UserLogin,
    authorize: AuthJWT = Depends(),
    service: UserService = Depends(UserService),
):
    if user := await service.login_user(user_login):
        access_token = authorize.create_access_token(subject=user.id)
        return {"access_token": access_token}
    raise HTTPException(status_code=401, detail="Bad username or password")


@router.get('')
def get_current_user(user_id: int = Depends(get_current_user_id), service: UserService = Depends(UserService)):
    user = service.get_user_by_id(user_id)
    return user
