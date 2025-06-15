from uuid import UUID
from fastapi import APIRouter, HTTPException

from ..data import SAMPLE_INDICATORS
from ..risk_engine import calculate_risk_level, normalize_score, aggregate_scores
from ..models import EvaluationResult, Thresholds

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


@router.get("/indicators/{indicator_id}/score", response_model=EvaluationResult)
def indicator_score(indicator_id: UUID, value: float) -> EvaluationResult:
    for ind in SAMPLE_INDICATORS:
        if ind.id == indicator_id:
            level = calculate_risk_level(value, ind.thresholds)
            score = normalize_score(value, ind.thresholds)
            return EvaluationResult(normalized_score=score, risk_level=level)
    raise HTTPException(status_code=404, detail="Indicator not found")


@router.post("/aggregate", response_model=EvaluationResult)
def aggregate(values: dict[UUID, float]) -> EvaluationResult:
    scores = []
    for ind in SAMPLE_INDICATORS:
        if ind.id in values:
            score = normalize_score(values[ind.id], ind.thresholds)
            scores.append((score, ind.weight))
    if not scores:
        raise HTTPException(status_code=400, detail="No matching indicators")
    overall_score = aggregate_scores(scores)
    # Use generic thresholds for aggregation
    level = calculate_risk_level(overall_score, Thresholds(low=25, medium=50, high=75, critical=90))
    return EvaluationResult(normalized_score=overall_score, risk_level=level)
