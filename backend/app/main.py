from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.users.router import router as auth_router
from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title="Sweet Shop Management API",
        lifespan=lifespan,
    )
    app.include_router(auth_router)
    return app

app = create_app()
