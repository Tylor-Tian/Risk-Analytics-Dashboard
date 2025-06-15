from fastapi import APIRouter
from ..services import list_indicators as list_indicators_service


router = APIRouter()


@router.get("/indicators")
def list_indicators():
    return list_indicators_service()
