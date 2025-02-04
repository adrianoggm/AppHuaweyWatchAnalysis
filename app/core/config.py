import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Huawei Watch Backend"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    PROJECT_DESCRIPTION: str = "API para la aplicación Huawei Watch"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    HUAWEI_CLIENT_ID: str
    HUAWEI_CLIENT_SECRET: str
    HUAWEI_REDIRECT_URI: str

    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
