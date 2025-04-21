from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.api import notes, ping
from app.db import database, engine, metadata

metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: connect to the database
    await database.connect()
    yield
    # Shutdown: disconnect from the database
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
