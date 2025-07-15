from fastapi import APIRouter

router = APIRouter()

@router.get("/download/ping")
def ping():
    return {"msg": "download route ok"}
