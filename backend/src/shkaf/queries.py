from collections.abc import Sequence
from datetime import date
from typing import Type, TypeVar
from uuid import UUID

from sqlalchemy import select

from shkaf.db import SessionDep
from shkaf.models import Outfit, OutfitOfTheDay, TranslatedModel, UUIDModel

T = TypeVar("T", bound=UUIDModel)
U = TypeVar("U")
TR = TypeVar("TR", bound=TranslatedModel)


async def get_by_ids(model: Type[T], ids: list[UUID], db: SessionDep) -> Sequence[T]:
    stmt = select(model).where(model.id.in_(ids))
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_user_data(model: Type[U], user_id: UUID, db: SessionDep) -> Sequence[U]:
    stmt = select(model).where(model.user_id == user_id)  # type: ignore
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_user_data_by_id(model: Type[U], user_id: UUID, id: UUID, db: SessionDep) -> U | None:
    stmt = select(model).where(model.user_id == user_id, model.id == id)  # type: ignore
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_user_data_by_ids(
    model: Type[U], user_id: UUID, ids: list[UUID], db: SessionDep
) -> Sequence[U]:
    stmt = select(model).where(model.user_id == user_id, model.id.in_(ids))  # type: ignore
    result = await db.execute(stmt)
    return result.scalars().all()


async def create_translated_model_entity(
    model: Type[TR], user_id: UUID, db: SessionDep, **data: dict
) -> TR:
    entity = model(user_id=user_id, **data)
    db.add(entity)
    await db.commit()
    await db.refresh(entity)
    return entity


async def get_outfits_by_closet_id_ordered_by_creation_date(
    closet_id: UUID, db: SessionDep
) -> Sequence[Outfit]:
    stmt = select(Outfit).where(Outfit.closet_id == closet_id).order_by(Outfit.created_at.desc())
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_outfit_by_id_and_closet_id(
    outfit_id: UUID, closet_id: UUID, db: SessionDep
) -> Outfit | None:
    stmt = select(Outfit).where(Outfit.id == outfit_id, Outfit.closet_id == closet_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_ootds_by_closet_id_and_date_range(
    closet_id: UUID, date_from: date, date_to: date, db: SessionDep
) -> Sequence[OutfitOfTheDay]:
    stmt = (
        select(OutfitOfTheDay)
        .where(
            OutfitOfTheDay.closet_id == closet_id,
            OutfitOfTheDay.date >= date_from,
            OutfitOfTheDay.date <= date_to,
        )
        .order_by(OutfitOfTheDay.date.desc())
    )
    result = await db.execute(stmt)
    return result.scalars().all()
