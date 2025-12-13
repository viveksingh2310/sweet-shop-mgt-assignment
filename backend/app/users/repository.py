from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.users.models import User
from app.db.database import AsyncSessionLocal

async def create_user(
    session: AsyncSession,
    email: str,
    password: str,
) -> User:
    user = User(email=email, password=password)
    session.add(user)
    await session.flush()  
    return user
async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User | None:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    return result.scalar_one_or_none()
# async def get_user_by_email(email: str) -> User | None:
#     async with AsyncSessionLocal() as session:
#         result = await session.execute(
#             select(User).where(User.email == email)
#         )
#         return result.scalar_one_or_none()

