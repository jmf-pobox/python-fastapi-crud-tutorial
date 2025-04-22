from collections.abc import Sequence
from typing import cast

from databases.interfaces import Record

from fastapi_crud_tutorial.db.db import database, notes
from fastapi_crud_tutorial.schemas.notes import NoteCreate


async def post(payload: NoteCreate) -> int:
    query_stmt = notes.insert().values(
        title=payload.title, description=payload.description
    )
    result = await database.execute(query=query_stmt)
    return cast(int, result)


async def get(id: int) -> Record | None:
    query_stmt = notes.select().where(id == notes.c.id)  # type: ignore
    return await database.fetch_one(query=query_stmt)


async def get_all() -> Sequence[Record]:
    query_stmt = notes.select()
    return await database.fetch_all(query=query_stmt)


async def put(id: int, payload: NoteCreate) -> int:
    query_stmt = (
        notes.update()
        .where(id == notes.c.id)  # type: ignore
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    result = await database.execute(query=query_stmt)
    return cast(int, result)


async def delete(id: int) -> int:
    query_stmt = notes.delete().where(id == notes.c.id)  # type: ignore
    result = await database.execute(query=query_stmt)
    return cast(int, result)
