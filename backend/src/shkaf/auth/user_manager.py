import uuid
from typing import Annotated, AsyncGenerator

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from shkaf.auth.dependencies import UsersDep
from shkaf.models import User

SECRET = "SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        # TODO: create closet
        await super().on_after_register(user, request)


async def get_user_manager(user_db: UsersDep) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)


UserManagerDep = Annotated[UserManager, Depends(get_user_manager)]
