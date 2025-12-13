from sqlalchemy import select,and_
from app.sweets.models import Sweet

async def create_sweet(session, data):
    sweet = Sweet(**data)
    session.add(sweet)
    await session.commit()
    await session.refresh(sweet)
    return sweet

async def list_sweets(session):
    result = await session.execute(select(Sweet))
    return result.scalars().all()

async def get_sweet_by_id(session, sweet_id):
    return await session.get(Sweet, sweet_id)

async def search_sweets(
    session,
    name: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
):
    conditions = []

    if name:
        conditions.append(Sweet.name.ilike(f"%{name}%"))

    if category:
        conditions.append(Sweet.category == category)

    if min_price is not None:
        conditions.append(Sweet.price >= min_price)

    if max_price is not None:
        conditions.append(Sweet.price <= max_price)

    query = select(Sweet)

    if conditions:
        query = query.where(and_(*conditions))

    result = await session.execute(query)
    return result.scalars().all()
