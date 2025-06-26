from datetime import date as pyDate
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID as pyUUID
from uuid import uuid4

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Table
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import UUID, Boolean, Date, String


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


class UUIDModel(AuditModel):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4, nullable=False)


class TranslatedModel(UUIDModel):
    __abstract__ = True

    name_en: Mapped[str]
    name_mk: Mapped[Optional[str]]


class User(SQLAlchemyBaseUserTableUUID, AuditModel):
    __tablename__ = "users"

    closet: Mapped["Closet"] = relationship(uselist=False)


class AccessToken(SQLAlchemyBaseAccessTokenTable[pyUUID], Base):
    __tablename__ = "access_tokens"

    user_id: Mapped[pyUUID] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="cascade"), nullable=False
    )


class Closet(UUIDModel):
    __tablename__ = "closets"

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
    Column("outfit_id", ForeignKey("outfits.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "clothing_piece_id", ForeignKey("clothing_pieces.id", ondelete="CASCADE"), primary_key=True
    ),
)
clothing_pieces_colors = Table(
    "clothing_pieces_colors",
    Base.metadata,
    Column(
        "clothing_piece_id", ForeignKey("clothing_pieces.id", ondelete="CASCADE"), primary_key=True
    ),
    Column("color_id", ForeignKey("colors.id", ondelete="CASCADE"), primary_key=True),
)
clothing_pieces_weather_seasons = Table(
    "clothing_pieces_weather_seasons",
    Base.metadata,
    Column(
        "clothing_piece_id", ForeignKey("clothing_pieces.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "weather_season_id", ForeignKey("weather_seasons.id", ondelete="CASCADE"), primary_key=True
    ),
)
clothing_pieces_fabric = Table(
    "clothing_pieces_fabric",
    Base.metadata,
    Column(
        "clothing_piece_id", ForeignKey("clothing_pieces.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "fabric_id", ForeignKey("clothing_piece_fabric.id", ondelete="CASCADE"), primary_key=True
    ),
)


class ClothingPieceStatusAssociation(Base):
    __tablename__ = "clothing_pieces_statuses"

    clothing_piece_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("clothing_pieces.id", ondelete="CASCADE"), primary_key=True
    )
    status_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("clothing_piece_status.id", ondelete="CASCADE"), primary_key=True
    )
    date: Mapped[pyDate] = mapped_column(Date, nullable=False, default=pyDate.today)
    is_current: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    clothing_piece: Mapped["ClothingPiece"] = relationship(back_populates="status_associations")
    status: Mapped["ClothingPieceStatus"] = relationship()


class ClothingPiece(UUIDModel):
    __tablename__ = "clothing_pieces"

    descriptor: Mapped[str]
    brand: Mapped[str]
    purchase_date: Mapped[Optional[pyDate]]
    place_of_purchase: Mapped[Optional[str]]
    price: Mapped[Optional[float]]
    price_currency: Mapped[Optional[str]]
    tags: Mapped[str]  # coma-separated
    comment: Mapped[Optional[str]]
    favorite: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    closet_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("closets.id", ondelete="CASCADE"), nullable=False
    )
    size_id: Mapped[Optional[UUID]] = mapped_column(
        UUID, ForeignKey("clothing_piece_size.id", ondelete="SET NULL"), nullable=True
    )

    size: Mapped[Optional["ClothingPieceSize"]] = relationship(uselist=False)
    outfits: Mapped[list["Outfit"]] = relationship(
        secondary=outfit_clothing_pieces,
        back_populates="clothing_pieces",
    )
    colors: Mapped[list["Color"]] = relationship(
        secondary=clothing_pieces_colors,
    )
    weather_seasons: Mapped[list["WeatherSeason"]] = relationship(
        secondary=clothing_pieces_weather_seasons,
    )
    status_associations: Mapped[list["ClothingPieceStatusAssociation"]] = relationship(
        back_populates="clothing_piece", cascade="all, delete-orphan"
    )
    fabric: Mapped[list["ClothingPieceFabric"]] = relationship(
        secondary=clothing_pieces_fabric,
    )

    @property
    def current_statuses(self) -> list["ClothingPieceStatus"]:
        return [assoc.status for assoc in self.status_associations if assoc.is_current]


class Outfit(UUIDModel):
    __tablename__ = "outfits"

    closet_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("closets.id", ondelete="CASCADE"), nullable=False
    )

    clothing_pieces: Mapped[list[ClothingPiece]] = relationship(
        secondary=outfit_clothing_pieces, back_populates="outfits"
    )
    ootds: Mapped[list["OutfitOfTheDay"]] = relationship(back_populates="outfit")


class OutfitOfTheDay(UUIDModel):
    __tablename__ = "ootds"

    date: Mapped[pyDate] = mapped_column(Date, default=pyDate.today, nullable=False)

    outfit_id: Mapped[UUID] = mapped_column(
        ForeignKey("outfits.id", ondelete="CASCADE"), nullable=False
    )
    closet_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("closets.id", ondelete="CASCADE"), nullable=False
    )

    outfit: Mapped[Outfit] = relationship(back_populates="ootds")


class Color(TranslatedModel):  # TODO: create initial rows
    __tablename__ = "colors"

    hex: Mapped[str]


class WeatherSeason(TranslatedModel):  # TODO: create initial rows
    __tablename__ = "weather_seasons"


class ClothingPieceStatus(TranslatedModel):  # TODO: create initial rows
    __tablename__ = "clothing_piece_status"


class ClothingPieceFabric(TranslatedModel):  # TODO: create initial rows
    __tablename__ = "clothing_piece_fabric"


class ClothingPieceSize(TranslatedModel):  # TODO: create initial rows
    __tablename__ = "clothing_piece_size"
