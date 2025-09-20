from typing import Annotated, Any

from fastapi import APIRouter, Form

from shkaf.auth.main import CurrentUserDep
from shkaf.db import SessionDep
from shkaf.models import (
    ClothingPiece,
    ClothingPieceFabric,
    ClothingPieceStatus,
    ClothingPieceStatusAssociation,
    Color,
    Outfit,
    OutfitAesthetic,
    OutfitOccasion,
    WeatherSeason,
)
from shkaf.queries import (
    get_by_ids,
    get_outfits_by_closet_id_ordered_by_creation_date,
    get_user_data_by_id,
    get_user_data_by_ids,
)
from shkaf.schema.request import ClothingPieceCreate, OutfitCreate
from shkaf.schema.response import ClosetResponse, ClothingPieceResponse, OutfitResponse
from shkaf.utils import save_image

router = APIRouter()


@router.get("/me", response_model=ClosetResponse)
async def get_my_closet(user: CurrentUserDep) -> Any:
    return user.closet


@router.post("/me/add-piece", response_model=ClothingPieceResponse)
async def add_piece_to_my_closet(
    data: Annotated[ClothingPieceCreate, Form(media_type="multipart/form-data")],
    user: CurrentUserDep,
    db: SessionDep,
) -> Any:
    image_path = save_image(data.image)
    colors = await get_user_data_by_ids(Color, user.id, data.colors_ids or [], db)
    weather_seasons = await get_user_data_by_ids(
        WeatherSeason, user.id, data.weather_seasons_ids or [], db
    )
    fabric = await get_user_data_by_ids(ClothingPieceFabric, user.id, data.fabrics_ids or [], db)
    primitive_piece_data = data.model_dump(
        exclude={
            "tags",
            "image",
            "colors_ids",
            "weather_seasons_ids",
            "statuses_ids",
            "fabrics_ids",
        }
    )

    clothing_piece = ClothingPiece(
        image_path=image_path,
        closet_id=user.closet.id,
        colors=colors,
        weather_seasons=weather_seasons,
        fabric=fabric,
        tags=",".join(data.tags) if data.tags else None,
        **primitive_piece_data,
    )
    db.add(clothing_piece)

    statuses = await get_user_data_by_ids(ClothingPieceStatus, user.id, data.statuses_ids or [], db)
    status_associations = [
        ClothingPieceStatusAssociation(clothing_piece=clothing_piece, status=status)
        for status in statuses
    ]
    db.add_all(status_associations)

    await db.commit()
    await db.refresh(
        clothing_piece,
        attribute_names=["size", "colors", "weather_seasons", "fabric", "status_associations"],
    )

    return clothing_piece


@router.post("/me/create-outfit", response_model=OutfitResponse)
async def create_outfit(
    data: Annotated[OutfitCreate, Form(media_type="multipart/form-data")],
    user: CurrentUserDep,
    db: SessionDep,
) -> Any:
    clothing_pieces = await get_by_ids(ClothingPiece, data.clothing_piece_ids, db)

    if any(piece.closet_id != user.closet.id for piece in clothing_pieces):
        raise ValueError("One or more clothing pieces do not belong to user's closet")

    occasion = None
    if data.occasion_id:
        occasion = await get_user_data_by_id(OutfitOccasion, user.id, data.occasion_id, db)

    aesthetic = None
    if data.aesthetic_id:
        aesthetic = await get_user_data_by_id(OutfitAesthetic, user.id, data.aesthetic_id, db)

    try_on_photo_path = None
    if data.try_on_photo:
        try_on_photo_path = save_image(data.try_on_photo)

    # Create outfit
    outfit = Outfit(
        name=data.name,
        closet_id=user.closet.id,
        occasion=occasion,
        aesthetic=aesthetic,
        try_on_photo_path=try_on_photo_path,
        clothing_pieces=clothing_pieces,
    )

    db.add(outfit)
    await db.commit()
    await db.refresh(
        outfit,
        attribute_names=["occasion", "aesthetic", "clothing_pieces"],
    )

    return outfit


@router.get("/me/outfits", response_model=list[OutfitResponse])
async def get_my_outfits(user: CurrentUserDep, db: SessionDep) -> Any:
    outfits = await get_outfits_by_closet_id_ordered_by_creation_date(user.closet.id, db)
    return outfits
