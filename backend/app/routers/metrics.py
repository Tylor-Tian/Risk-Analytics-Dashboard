from fastapi import APIRouter

router = APIRouter()

@router.get("/overview")
def metrics_overview():
    return {}

