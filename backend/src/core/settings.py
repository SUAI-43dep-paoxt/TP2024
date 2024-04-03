from fastapi_jwt_auth import AuthJWT
from pydantic import BaseSettings


class Settings(BaseSettings):
    authjwt_secret_key: str = "secret"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/app"


@AuthJWT.load_config
def get_settings() -> Settings:
    return Settings()
