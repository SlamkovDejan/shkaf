from typing import Annotated, Any

from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

from shkaf.auth.main import CurrentUserDep, auth_backend, fastapi_users
from shkaf.auth.schemas import UserCreate, UserRead, UserUpdate
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
from shkaf.routers import data_router
from shkaf.schema.request import ClothingPieceCreate
from shkaf.schema.response import (
    ClosetResponse,
    ClothingPieceResponse,
)
from shkaf.utils import save_image

app = FastAPI()

app.mount("/images", StaticFiles(directory="public/images"), name="images")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
# custom routers
app.include_router(data_router, prefix="/data", tags=["data"])


@app.get("/")
async def root() -> dict:
    return {"Hello": "World"}


@app.get("/authorized")
async def authorized_root(user: CurrentUserDep) -> dict:
    return {"Hello": "World", "mail": user.email}


@app.get("/closet/me", tags=["closet"], response_model=ClosetResponse)
async def get_my_closet(user: CurrentUserDep) -> Any:
    return user.closet


@app.post("/closet/me/add-piece", tags=["closet"], response_model=ClothingPieceResponse)
async def add_piece_to_closet(
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
        tags=",".join(data.tags),
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
