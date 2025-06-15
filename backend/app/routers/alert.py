from fastapi import APIRouter
from ..services import list_alerts as list_alerts_service

router = APIRouter()


@router.get("/")
def list_alerts():
    return list_alerts_service()
