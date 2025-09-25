from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field, field_serializer


class TranslatedModelResponse(BaseModel):
    id: UUID
    name_en: str
    name_mk: str | None = None

    class Config:
        from_attributes = True


class ColorResponse(TranslatedModelResponse):
    hex: str

    class Config:
        from_attributes = True


class ClothingPieceResponse(BaseModel):
    id: UUID
    image_path: str
    image_no_bg_path: str | None = None
    descriptor: str
    brand: str | None = None
    purchase_date: date | None = None
    price: float | None = None
    price_currency: str | None = None
    tags: str | None = None
    comment: str | None = None
    favorite: bool

    size: TranslatedModelResponse | None = None
    colors: list[ColorResponse]
    weather_seasons: list[TranslatedModelResponse]
    current_statuses: list[TranslatedModelResponse] = Field(serialization_alias="statuses")
    fabric: list[TranslatedModelResponse]

    @field_serializer("current_statuses")
    def get_statuses(self, value: list) -> list[TranslatedModelResponse]:
        return [TranslatedModelResponse.model_validate(status) for status in value]

    @field_serializer("tags")
    def serialize_tags(self, value: str) -> list[str]:
        return value.split(",") if value else []

    class Config:
        from_attributes = True


class OutfitResponse(BaseModel):
    id: UUID
    name: str | None = None
    created_at: datetime
    try_on_photo_path: str | None = None
    occasion: TranslatedModelResponse | None = None
    aesthetic: TranslatedModelResponse | None = None
    clothing_pieces: list[ClothingPieceResponse]

    class Config:
        from_attributes = True


class OutfitOfTheDayResponse(BaseModel):
    id: UUID
    date: date
    outfit: OutfitResponse

    class Config:
        from_attributes = True


class OOTDCalendarResponse(BaseModel):
    date: date
    ootds: list[OutfitOfTheDayResponse]


class ClosetResponse(BaseModel):
    id: UUID
    name: str
    clothing_pieces: list[ClothingPieceResponse]

    class Config:
        from_attributes = True
