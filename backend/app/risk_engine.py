from typing import Iterable, Literal, Tuple

from .models import Thresholds

RiskLevel = Literal['low', 'medium', 'high', 'critical']

def calculate_risk_level(value: float, thresholds: Thresholds) -> RiskLevel:
    if value >= thresholds.critical:
        return 'critical'
    if value >= thresholds.high:
        return 'high'
    if value >= thresholds.medium:
        return 'medium'
    return 'low'


def normalize_score(value: float, thresholds: Thresholds) -> float:
    """Normalize a raw value to a 0-100 score based on the critical threshold."""
    if thresholds.critical == 0:
        return 0.0
    score = (value / thresholds.critical) * 100
    return max(0.0, min(score, 100.0))


def aggregate_scores(scores: Iterable[Tuple[float, float]]) -> float:
    """Return weighted average of scores given as (score, weight)."""
    scores = list(scores)
    total_weight = sum(w for _, w in scores)
    if total_weight == 0:
        return 0.0
    return sum(s * w for s, w in scores) / total_weight
