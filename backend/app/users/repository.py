from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.users.models import User


async def create_user(
    session: AsyncSession,
    email: str,
    password: str,
) -> User:
    user = User(email=email, password=password)
    session.add(user)
    await session.flush()  # Let DB raise constraint errors
    return user
