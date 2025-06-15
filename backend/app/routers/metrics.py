from fastapi import APIRouter
from ..services import overview as metrics_overview_service

router = APIRouter()

@router.get("/overview")
def metrics_overview():
    return metrics_overview_service()

