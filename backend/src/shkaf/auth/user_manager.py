import uuid
from typing import Annotated, AsyncGenerator

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from shkaf.auth.dependencies import UsersDep
from shkaf.config import AUTH_SECRET
from shkaf.db import async_session_maker
from shkaf.models import User
from shkaf.seed import register_user_seed


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = AUTH_SECRET
    verification_token_secret = AUTH_SECRET

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        await super().on_after_register(user, request)
        async with async_session_maker() as session:
            await register_user_seed(user.id, session)


async def get_user_manager(user_db: UsersDep) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)


UserManagerDep = Annotated[UserManager, Depends(get_user_manager)]
