from typing import Annotated, Any, AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from shkaf.db import Base, SessionDep


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


async def get_user_db(
    session: SessionDep,
) -> AsyncGenerator[SQLAlchemyUserDatabase[User, Any], None]:
    yield SQLAlchemyUserDatabase(session, User)


UsersDep = Annotated[SQLAlchemyUserDatabase[User, Any], Depends(get_user_db)]
