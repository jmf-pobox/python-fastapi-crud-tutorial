from datetime import datetime

from pydantic import BaseModel


class Note(BaseModel):
    """Domain model for a note."""

    id: int
    title: str
    description: str
    created_date: datetime

    class Config:
        """Pydantic config for the model."""

        from_attributes = True
