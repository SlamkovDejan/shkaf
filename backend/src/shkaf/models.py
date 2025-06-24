from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID as pyUUID

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import UUID


class Base(DeclarativeBase):
    pass


class AuditModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class User(SQLAlchemyBaseUserTableUUID, AuditModel):
    __tablename__ = "users"


class AccessToken(SQLAlchemyBaseAccessTokenTable[pyUUID], Base):
    __tablename__ = "access_tokens"

    user_id: Mapped[pyUUID] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="cascade"), nullable=False
    )
