from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app.db.database import AsyncSessionLocal
from app.users.models import User


async def create_user(email: str, password: str):
    async with AsyncSessionLocal() as session:
        user = User(email=email, password=password)
        session.add(user)

        try:
            await session.commit()
            await session.refresh(user)
            return user

        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
