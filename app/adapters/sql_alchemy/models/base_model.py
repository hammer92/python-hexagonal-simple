from datetime import datetime

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.functions import now


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=now())
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=now(), onupdate=now())

class Base(DeclarativeBase):
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}