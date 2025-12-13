from fastapi import APIRouter,Depends
from pydantic import BaseModel
from app.users.schemas import LoginRequest, TokenResponse
from app.users.service import register_user, authenticate_user
from app.users.models import User
from app.core.dependencies import get_current_user
router = APIRouter(prefix="/api/auth", tags=["auth"])


class AuthPayload(BaseModel):
    email: str
    password: str


@router.post("/register", status_code=201)
async def register(payload: AuthPayload):
    return await register_user(payload.email, payload.password)

@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest):
    return await authenticate_user(
        payload.email,
        payload.password,
    )
@router.get("/me")
async def read_profile(
    current_user: User = Depends(get_current_user),
):
    return {
        "email": current_user.email,
        "id": current_user.id,
    }

