from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from shkaf.auth.dependencies import AccessTokenDep


def get_database_strategy(access_token_db: AccessTokenDep) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


bearer_transport = BearerTransport(tokenUrl="auth/login")


auth_backend = AuthenticationBackend(
    name="bearer",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
