import os

from pydantic import  Field
from pydantic_settings import BaseSettings

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(ROOT_DIR,"..","..", '.env.local')

class Settings(BaseSettings):
    VERSION: str = Field("0.0.1")
    PROJECT_NAME: str = Field("Ultimate FastAPI Project Setup")
    DATABASE_USER: str = Field("postgres")
    DATABASE_PASSWORD: str = Field("postgres")
    DATABASE_DB: str = Field("postgres")
    DATABASE_HOST: str = Field("localhost")
    DATABASE_DRIVERNAME: str = Field("postgress")
    DATABASE_PORT: int | str = Field("5432")
    DATABASE_POOL_SIZE: int = Field(10)

    class Config:
        case_sensitive = True
        env_file = csv_path


settings = Settings()
