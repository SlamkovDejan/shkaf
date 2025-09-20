from typing import Any

from fastapi import APIRouter

from shkaf.auth.main import CurrentUserDep
from shkaf.db import SessionDep
from shkaf.models import (
    ClothingPieceFabric,
    ClothingPieceSize,
    ClothingPieceStatus,
    Color,
    OutfitAesthetic,
    OutfitOccasion,
    WeatherSeason,
)
from shkaf.queries import create_translated_model_entity, get_user_data
from shkaf.schema.request import ColorCreate, TranslatedModelCreate
from shkaf.schema.response import ColorResponse, TranslatedModelResponse

router = APIRouter()


@router.post("/colors", response_model=ColorResponse)
async def create_color(data: ColorCreate, user: CurrentUserDep, db: SessionDep) -> Any:
    return await create_translated_model_entity(Color, user.id, db, **data.model_dump())


@router.get("/colors", response_model=list[ColorResponse])
async def get_colors(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(Color, user.id, db)


@router.post("/clothing-piece-sizes", response_model=TranslatedModelResponse)
async def create_clothing_piece_size(
    data: TranslatedModelCreate, user: CurrentUserDep, db: SessionDep
) -> Any:
    return await create_translated_model_entity(ClothingPieceSize, user.id, db, **data.model_dump())


@router.get("/clothing-piece-sizes", response_model=list[TranslatedModelResponse])
async def get_clothing_piece_sizes(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(ClothingPieceSize, user.id, db)


@router.post("/clothing-piece-fabrics", response_model=TranslatedModelResponse)
async def create_clothing_piece_fabric(
    data: TranslatedModelCreate, user: CurrentUserDep, db: SessionDep
) -> Any:
    return await create_translated_model_entity(
        ClothingPieceFabric, user.id, db, **data.model_dump()
    )


@router.get("/clothing-piece-fabrics", response_model=list[TranslatedModelResponse])
async def get_clothing_piece_fabrics(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(ClothingPieceFabric, user.id, db)


@router.post("/clothing-piece-statuses", response_model=TranslatedModelResponse)
async def create_clothing_piece_status(
    data: TranslatedModelCreate, user: CurrentUserDep, db: SessionDep
) -> Any:
    return await create_translated_model_entity(
        ClothingPieceStatus, user.id, db, **data.model_dump()
    )


@router.get("/clothing-piece-statuses", response_model=list[TranslatedModelResponse])
async def get_clothing_piece_statuses(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(ClothingPieceStatus, user.id, db)


@router.post("/weather-seasons", response_model=TranslatedModelResponse)
async def create_weather_season(
    data: TranslatedModelCreate, user: CurrentUserDep, db: SessionDep
) -> Any:
    return await create_translated_model_entity(WeatherSeason, user.id, db, **data.model_dump())


@router.get("/weather-seasons", response_model=list[TranslatedModelResponse])
async def get_weather_seasons(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(WeatherSeason, user.id, db)


@router.post("/outfit-aesthetics", response_model=TranslatedModelResponse)
async def create_outfit_aesthetic(
    data: TranslatedModelCreate, user: CurrentUserDep, db: SessionDep
) -> Any:
    return await create_translated_model_entity(OutfitAesthetic, user.id, db, **data.model_dump())


@router.get("/outfit-aesthetics", response_model=list[TranslatedModelResponse])
async def get_outfit_aesthetics(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(OutfitAesthetic, user.id, db)


@router.post("/outfit-occasions", response_model=TranslatedModelResponse)
async def create_outfit_occasion(
    data: TranslatedModelCreate, user: CurrentUserDep, db: SessionDep
) -> Any:
    return await create_translated_model_entity(OutfitOccasion, user.id, db, **data.model_dump())


@router.get("/outfit-occasions", response_model=list[TranslatedModelResponse])
async def get_outfit_occasions(user: CurrentUserDep, db: SessionDep) -> Any:
    return await get_user_data(OutfitOccasion, user.id, db)
