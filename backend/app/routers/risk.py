from fastapi import APIRouter

router = APIRouter()

@router.get("/indicators")
def list_indicators():
    return []

