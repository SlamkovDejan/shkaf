from datetime import date as pyDate
from datetime import datetime, timezone
from uuid import UUID as pyUUID
from uuid import uuid4

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Table
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import UUID, Date, String


class Base(AsyncAttrs, DeclarativeBase):
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

    closet: Mapped["Closet"] = relationship(uselist=False)


class AccessToken(SQLAlchemyBaseAccessTokenTable[pyUUID], Base):
    __tablename__ = "access_tokens"

    user_id: Mapped[pyUUID] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="cascade"), nullable=False
    )


class Closet(AuditModel):
    __tablename__ = "closets"

    id: Mapped[pyUUID] = mapped_column(UUID, primary_key=True, default=uuid4, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )

    clothing_pieces: Mapped[list["ClothingPiece"]] = relationship()
    outfits: Mapped[list["Outfit"]] = relationship()
    ootds: Mapped[list["OutfitOfTheDay"]] = relationship()


outfit_clothing_pieces = Table(
    "outfit_clothing_pieces",
    Base.metadata,
    Column("outfit_id", ForeignKey("outfits.id"), primary_key=True),
    Column("clothing_piece_id", ForeignKey("clothing_pieces.id"), primary_key=True),
)


class ClothingPiece(AuditModel):
    __tablename__ = "clothing_pieces"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4, nullable=False)

    closet_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("closets.id", ondelete="CASCADE"), nullable=False
    )

    outfits: Mapped[list["Outfit"]] = relationship(
        secondary=outfit_clothing_pieces,
        back_populates="clothing_pieces",
    )


class Outfit(AuditModel):
    __tablename__ = "outfits"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4, nullable=False)

    closet_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("closets.id", ondelete="CASCADE"), nullable=False
    )

    clothing_pieces: Mapped[list[ClothingPiece]] = relationship(
        secondary=outfit_clothing_pieces, back_populates="outfits"
    )
    ootds: Mapped[list["OutfitOfTheDay"]] = relationship(back_populates="outfit")


class OutfitOfTheDay(AuditModel):
    __tablename__ = "ootds"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4, nullable=False)
    date: Mapped[pyDate] = mapped_column(Date, default=pyDate.today, nullable=False)

    outfit_id: Mapped[UUID] = mapped_column(
        ForeignKey("outfits.id", ondelete="CASCADE"), nullable=False
    )
    closet_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("closets.id", ondelete="CASCADE"), nullable=False
    )

    outfit: Mapped[Outfit] = relationship(back_populates="ootds")
