from uuid import UUID
from fastapi import APIRouter, HTTPException

from ..data import SAMPLE_INDICATORS
from ..risk_engine import calculate_risk_level

router = APIRouter()


@router.get("/indicators")
def list_indicators():
    return SAMPLE_INDICATORS


@router.get("/indicators/{indicator_id}")
def get_indicator(indicator_id: UUID):
    for ind in SAMPLE_INDICATORS:
        if ind.id == indicator_id:
            return ind
    raise HTTPException(status_code=404, detail="Indicator not found")


@router.get("/indicators/{indicator_id}/score")
def indicator_score(indicator_id: UUID, value: float):
    for ind in SAMPLE_INDICATORS:
        if ind.id == indicator_id:
            level = calculate_risk_level(value, ind.thresholds)
            return {"level": level}
    raise HTTPException(status_code=404, detail="Indicator not found")
