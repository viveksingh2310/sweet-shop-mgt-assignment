from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.users.models import User


async def create_user(
    session: AsyncSession,
    email: str,
    password: str,
) -> User:
    user = User(email=email, password=password)
    session.add(user)
    await session.flush()  
    return user
async def get_user_by_email(session: AsyncSession,
    email: str,) -> User | None:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    return result.scalar_one_or_none()

