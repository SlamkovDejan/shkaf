from datetime import date
from typing import Any
from uuid import UUID

from fastapi import UploadFile
from pydantic import BaseModel, field_validator


class ClothingPieceCreate(BaseModel):
    image: UploadFile
    descriptor: str
    brand: str | None = None
    purchase_date: date | None = None
    place_of_purchase: str | None = None
    price: float | None = None
    price_currency: str | None = None
    tags: list[str] | None = None
    comment: str | None = None
    favorite: bool = False

    size_id: UUID | None = None
    colors_ids: list[UUID] | None = None
    weather_seasons_ids: list[UUID] | None = None
    statuses_ids: list[UUID] | None = None
    fabrics_ids: list[UUID] | None = None

    @field_validator(
        "colors_ids", "weather_seasons_ids", "statuses_ids", "fabrics_ids", mode="before"
    )
    @classmethod
    def split_uuid_csv(cls, v: Any) -> list[UUID]:
        def split_and_strip(item: str) -> list[UUID]:
            parts = item.split(",")
            return [UUID(item.strip()) for item in parts if item.strip()]

        if isinstance(v, list):
            return [parsed_item for item in v for parsed_item in split_and_strip(item)]
        if isinstance(v, str):
            return split_and_strip(v)
        return []

    @field_validator("tags", mode="before")
    @classmethod
    def split_str_csv(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [item.strip() for item in v.split(",")]
        if isinstance(v, list):
            return [parsed_item.strip() for item in v for parsed_item in item.split(",")]
        return []


class TranslatedModelCreate(BaseModel):
    name_en: str
    name_mk: str | None = None


class ColorCreate(TranslatedModelCreate):
    hex: str


class OutfitCreate(BaseModel):
    name: str | None = None
    clothing_piece_ids: list[UUID]
    occasion_id: UUID | None = None
    aesthetic_id: UUID | None = None
    try_on_photo: UploadFile | None = None

    @field_validator("clothing_piece_ids", mode="before")
    @classmethod
    def split_uuid_csv(cls, v: Any) -> list[UUID]:
        def split_and_strip(item: str) -> list[UUID]:
            parts = item.split(",")
            return [UUID(item.strip()) for item in parts if item.strip()]

        if isinstance(v, list):
            return [parsed_item for item in v for parsed_item in split_and_strip(item)]
        if isinstance(v, str):
            return split_and_strip(v)
        return []
