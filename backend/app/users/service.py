from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.db.database import AsyncSessionLocal
from app.users.repository import create_user
from app.core.security import hash_password


async def register_user(email: str, password: str):
    hashed_password = hash_password(password)  # ✅ HASH HERE

    async with AsyncSessionLocal() as session:
        try:
            user = await create_user(
                session=session,
                email=email,
                password=hashed_password,  # ✅ STORE HASH
            )
            await session.commit()
            return user

        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
