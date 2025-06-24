from typing import Annotated, Any, AsyncGenerator

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
)

from shkaf.db import SessionDep
from shkaf.models import AccessToken, User


async def get_access_token_db(
    session: SessionDep,
) -> AsyncGenerator[SQLAlchemyAccessTokenDatabase[AccessToken], None]:
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


AccessTokenDep = Annotated[AccessTokenDatabase[AccessToken], Depends(get_access_token_db)]


async def get_user_db(
    session: SessionDep,
) -> AsyncGenerator[SQLAlchemyUserDatabase[User, Any], None]:
    yield SQLAlchemyUserDatabase(session, User)


UsersDep = Annotated[SQLAlchemyUserDatabase[User, Any], Depends(get_user_db)]
