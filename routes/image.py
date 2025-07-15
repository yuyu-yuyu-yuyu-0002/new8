from fastapi import APIRouter

router = APIRouter()

@router.get("/image/ping")
def ping():
    return {"msg": "image route ok"}
