from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.api.models import NoteDB, NoteSchema

router = APIRouter()


@router.get("/", response_model=list[NoteDB])
async def read_all_notes() -> list[NoteDB]:
    notes = await crud.get_all()
    return [
        NoteDB(
            id=note["id"],
            title=note["title"],
            description=note["description"],
        )
        for note in notes
    ]


@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema) -> NoteDB:
    note_id = await crud.post(payload)
    return NoteDB(
        id=note_id,
        title=payload.title,
        description=payload.description,
    )


@router.get("/{id}/", response_model=NoteDB)
async def read_note(
    id: int = Path(..., gt=0),
) -> NoteDB:
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteDB(
        id=note["id"],
        title=note["title"],
        description=note["description"],
    )


@router.put("/{id}/", response_model=NoteDB)
async def update_note(
    payload: NoteSchema,
    id: int = Path(..., gt=0),
) -> NoteDB:
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note_id = await crud.put(id, payload)
    return NoteDB(
        id=note_id,
        title=payload.title,
        description=payload.description,
    )


@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(
    id: int = Path(..., gt=0),
) -> NoteDB:
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await crud.delete(id)
    return NoteDB(
        id=note["id"],
        title=note["title"],
        description=note["description"],
    )
