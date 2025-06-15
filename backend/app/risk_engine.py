from typing import Literal

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
