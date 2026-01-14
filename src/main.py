from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import create_db_and_tables
from modules.shorts.router import router as shorts_router
from modules.tags.router import router as tags_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(shorts_router)
app.include_router(tags_router)