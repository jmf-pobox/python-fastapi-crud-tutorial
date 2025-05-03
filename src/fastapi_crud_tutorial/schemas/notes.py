from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    """Schema for creating a new note."""

    title: str = Field(
        ..., min_length=3, max_length=50, description="The title of the note"
    )
    description: str = Field(
        ..., min_length=3, max_length=50, description="The content of the note"
    )


class NoteUpdate(NoteCreate):
    """Schema for updating an existing note."""

    pass


class NoteResponse(NoteCreate):
    """Schema for note responses from the API."""

    id: int

    model_config = {"from_attributes": True}
