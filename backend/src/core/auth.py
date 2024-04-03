from fastapi import Depends
from fastapi_jwt_auth import AuthJWT


def get_current_user_id(
    authorize: AuthJWT = Depends(),
) -> int:
    authorize.jwt_required()

    user_id = authorize.get_jwt_subject()
    return user_id
