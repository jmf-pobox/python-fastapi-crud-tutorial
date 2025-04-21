from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong() -> dict[str, str]:
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}
