from fastapi import APIRouter, status
from app.users.schemas import UserCreate, UserResponse
from app.users.service import create_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(payload: UserCreate):
    user = await create_user(payload.email, payload.password)
    return UserResponse(id=user.id, email=user.email)
