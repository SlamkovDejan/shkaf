from typing import Annotated, AsyncGenerator

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)

from shkaf.db import Base, SessionDep


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass


async def get_access_token_db(
    session: SessionDep,
) -> AsyncGenerator[SQLAlchemyAccessTokenDatabase[AccessToken], None]:
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


AccessTokenDep = Annotated[AccessTokenDatabase[AccessToken], Depends(get_access_token_db)]
