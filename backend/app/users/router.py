from fastapi import APIRouter, status
from app.users.schemas import UserCreate
from app.users.service import register_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(payload: UserCreate):
    return await register_user(payload.email, payload.password)
