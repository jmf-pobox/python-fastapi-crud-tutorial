from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from fastapi_crud_tutorial.api import notes, ping
from fastapi_crud_tutorial.db.db import database, engine, metadata

metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: connect to the database
    await database.connect()
    yield
    # Shutdown: disconnect from the database
    await database.disconnect()


app = FastAPI(
    title="Notes API",
    description="A simple RESTful API for managing notes",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Your Name",
        "url": "http://example.com/contact/",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    lifespan=lifespan,
)

app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
