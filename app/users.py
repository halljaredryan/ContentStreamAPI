import uuid
import os
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, models, FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend, BearerTransport, JWTStrategy)
from app.db import User, get_user_db
from fastapi_users.db import SQLAlchemyUserDatabase
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get SECRET from environment variable
SECRET = os.getenv("SECRET")
if not SECRET:
    raise ValueError("SECRET environment variable is not set. Please set it in your .env file.")

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Token: {token}")

    async def on_after_verify_email(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has verified their email. Token: {token}")
    
async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)