from fastapi import APIRouter, HTTPException, Path

from fastapi_crud_tutorial.db import crud
from fastapi_crud_tutorial.models.models import NoteDB, NoteSchema

router = APIRouter()


@router.get(
    "/",
    response_model=list[NoteDB],
    summary="Get all notes",
    description="Retrieve a list of all notes from the database",
    response_description="List of notes successfully retrieved",
)
async def read_all_notes() -> list[NoteDB]:
    """
    Get all notes stored in the database.

    Returns:
        list[NoteDB]: A list of all notes, each containing:
        - **id**: The note's unique identifier
        - **title**: The note's title
        - **description**: The note's content
    """
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


@router.get(
    "/{id}/",
    response_model=NoteDB,
    responses={
        404: {
            "description": "Note not found",
            "content": {"application/json": {"example": {"detail": "Note not found"}}},
        }
    },
)
async def read_note(
    id: int = Path(..., gt=0, description="The ID of the note to retrieve"),
) -> NoteDB:
    """
    Retrieve a specific note by its ID.

    Args:
        id (int): The unique identifier of the note

    Raises:
        HTTPException: If the note is not found (404)

    Returns:
        NoteDB: The requested note
    """
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
