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
    WeatherSeason,
)
from shkaf.queries import get_by_ids
from shkaf.schema.request import ClothingPieceCreate
from shkaf.schema.response import ClosetResponse, ClothingPieceResponse
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
    colors = await get_by_ids(Color, data.colors_ids or [], db)
    weather_seasons = await get_by_ids(WeatherSeason, data.weather_seasons_ids or [], db)
    fabric = await get_by_ids(ClothingPieceFabric, data.fabrics_ids or [], db)
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

    statuses = await get_by_ids(ClothingPieceStatus, data.statuses_ids or [], db)
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
