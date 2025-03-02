from fastapi import APIRouter

router = APIRouter(tags=["status"])


@router.get("/status")
async def read_system_status():
    return {"status": "OK"}
