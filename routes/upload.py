from fastapi import APIRouter

router = APIRouter()

@router.get("/upload/ping")
def ping():
    return {"msg": "upload route ok"}
