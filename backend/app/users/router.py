from fastapi import APIRouter
from pydantic import BaseModel

from app.users.service import register_user, authenticate_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])


class AuthPayload(BaseModel):
    email: str
    password: str


@router.post("/register", status_code=201)
async def register(payload: AuthPayload):
    return await register_user(payload.email, payload.password)


@router.post("/login")
async def login(payload: AuthPayload):
    token = await authenticate_user(
        payload.email,
        payload.password,
    )
    return {
        "access_token": token,
        "token_type": "bearer",
    }
