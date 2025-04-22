from datetime import datetime

from pydantic import BaseModel


class Note(BaseModel):
    """Domain model for a note."""

    id: int
    title: str
    description: str
    created_date: datetime

    model_config = {
        "from_attributes": True
    }
