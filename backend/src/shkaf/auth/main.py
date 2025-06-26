import uuid
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from fastapi_users import FastAPIUsers

from shkaf.auth.backend import auth_backend
from shkaf.auth.user_manager import get_user_manager
from shkaf.db import SessionDep
from shkaf.models import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)

CurrentUserDep = Annotated[User, Depends(current_active_user)]


async def get_current_active_user_with_closet(
    session: SessionDep, user: CurrentUserDep
) -> AsyncGenerator[User, None]:
    await session.refresh(user, attribute_names=["closet"])
    yield user


UserWithClosetDep = Annotated[User, Depends(get_current_active_user_with_closet)]
