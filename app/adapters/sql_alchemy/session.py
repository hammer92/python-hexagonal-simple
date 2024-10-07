from os import environ

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from app.libraries.settings import settings


def create_pg_url(
    drivername: str = "postgresql",
    username: str = "postgres",
    password: str = "postgres",
    host: str = "localhost",
    port: str = "5432",
    database: str = "postgres",
) -> URL:
    return URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )


def create_pg_url_from_env(
    drivername: str | None = None,
    username: str | None = None,
    password: str | None = None,
    host: str | None = None,
    port: str | None = None,
    database: str | None = None,
) -> URL:
    return create_pg_url(
        drivername=drivername or settings.POSTGRES_DRIVERNAME,
        username=username or settings.POSTGRES_USER,
        password=password or settings.POSTGRES_PASSWORD,
        host=host or settings.POSTGRES_HOST,
        port=port or settings.POSTGRES_PORT,
        database=database or settings.POSTGRES_DB,
    )


url = create_pg_url_from_env(drivername="postgresql+asyncpg")
engine = create_async_engine(url)

SessionLocal = async_sessionmaker(
    engine,
    class_= AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    print("init get_session")
    async with SessionLocal() as session:
        try:
            result = await session.execute(text("select 1"))
            print(result)
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()