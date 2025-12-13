from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from app.users.models import User
from app.db.database import AsyncSessionLocal
from app.users.repository import create_user
from app.core.security import hash_password
from sqlalchemy.future import select
from app.core.security import verify_password
from app.core.jwt import create_access_token
from app.users.repository import get_user_by_email

async def register_user(email: str, password: str):
    hashed_password = hash_password(password) 

    async with AsyncSessionLocal() as session:
        try:
            user = await create_user(
                session=session,
                email=email,
                password=hashed_password, 
            )
            await session.commit()
            return user

        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
async def authenticate_user(email: str, password: str) -> dict:
    async with AsyncSessionLocal() as session:
        user = await get_user_by_email(session, email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        token = create_access_token(
            data={"sub": str(user.id)}
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
