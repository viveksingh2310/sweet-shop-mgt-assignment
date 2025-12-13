from app.db.database import AsyncSessionLocal
from app.users.models import User


async def create_user(email: str, password: str) -> User:
    async with AsyncSessionLocal() as session:
        user = User(email=email, password=password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
