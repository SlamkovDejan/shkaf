from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from shkaf.auth.main import CurrentUserDep, auth_backend, fastapi_users
from shkaf.auth.schemas import UserCreate, UserRead, UserUpdate
from shkaf.routers import closet_router, data_router, image_router

app = FastAPI()

app.mount("/images", StaticFiles(directory="public/images"), name="images")

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
# custom routers
app.include_router(closet_router, prefix="/closet", tags=["closet"])
app.include_router(data_router, prefix="/data", tags=["data"])
app.include_router(image_router, prefix="/image", tags=["image"])


@app.get("/")
async def root() -> dict:
    return {"Hello": "World"}


@app.get("/authorized")
async def authorized_root(user: CurrentUserDep) -> dict:
    return {"Hello": "World", "mail": user.email}
