from fastapi import FastAPI

from shkaf.auth.main import CurrentUserDep, UserWithClosetDep, auth_backend, fastapi_users
from shkaf.auth.schemas import UserCreate, UserRead, UserUpdate

app = FastAPI()


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


@app.get("/")
async def root() -> dict:
    return {"Hello": "World"}


@app.get("/authorized")
async def authorized_root(user: CurrentUserDep) -> dict:
    return {"Hello": "World", "mail": user.email}


@app.get("/closet/me", tags=["closet"])
async def get_my_closet(user: UserWithClosetDep) -> dict:
    # await session.refresh(user, attribute_names=["closet"])
    # await session.refresh(user, attribute_names=["closet"])
    # closet: Closet = await user.awaitable_attrs.closet
    print(user.closet)
    # cloting_pieces =
    return {"a": "b"}
