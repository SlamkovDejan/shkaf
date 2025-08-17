from collections.abc import Sequence
from typing import Type, TypeVar
from uuid import UUID

from sqlalchemy import select

from shkaf.db import SessionDep
from shkaf.models import UUIDModel

T = TypeVar("T", bound=UUIDModel)
U = TypeVar("U")


async def get_by_ids(model: Type[T], ids: list[UUID], db: SessionDep) -> Sequence[T]:
    stmt = select(model).where(model.id.in_(ids))
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_user_data(model: Type[U], user_id: UUID, db: SessionDep) -> Sequence[U]:
    stmt = select(model).where(model.user_id == user_id)  # type: ignore
    result = await db.execute(stmt)
    return result.scalars().all()
