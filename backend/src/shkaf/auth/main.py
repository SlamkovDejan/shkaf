import uuid
from typing import Annotated

from fastapi import Depends
from fastapi_users import FastAPIUsers

from shkaf.auth.backend import auth_backend
from shkaf.auth.user_manager import get_user_manager
from shkaf.models import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)

CurrentUserDep = Annotated[User, Depends(current_active_user)]
