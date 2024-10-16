# Import statements...
from asyncio import current_task

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncEngine

from app.libraries.settings import settings
print("------------", settings)
database_url = URL.create(
    drivername=settings.DATABASE_DRIVERNAME,
    database=settings.DATABASE_DB,
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
)

class DatabaseSessionManager:
    def __init__(self):
        self.engine: AsyncEngine | None = None
        self.session_maker = None
        self.session = None
        self.init_db()

    def init_db(self):
        # Database connection parameters...

        # Creating an asynchronous engine
        self.engine = create_async_engine(
            database_url,
            pool_size=settings.DATABASE_POOL_SIZE, max_overflow=20,
            pool_pre_ping=False
        )

        # Creating an asynchronous session class
        self.session_maker = async_sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        # Creating a scoped session
        self.session = async_scoped_session(self.session_maker, scopefunc=current_task)

    async def close(self):
        # Closing the database session...
        if self.engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self.engine.dispose()

