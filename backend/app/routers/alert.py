from uuid import UUID
from datetime import datetime
from fastapi import APIRouter

from ..data import SAMPLE_INDICATORS
from ..risk_engine import calculate_risk_level, normalize_score
from ..models import Alert

router = APIRouter()


@router.get("/")
def list_alerts(value: float = 0):
    alerts = []
    for ind in SAMPLE_INDICATORS:
        level = calculate_risk_level(value, ind.thresholds)
        score = normalize_score(value, ind.thresholds)
        if level in {"high", "critical"}:
            alerts.append(
                Alert(
                    id=UUID(int=0),
                    indicator_id=ind.id,
                    triggered_at=datetime.utcnow(),
                    severity="critical" if level == "critical" else "warning",
                    title=f"{ind.name} threshold breached",
                    description=f"Value {value} (score {score:.1f}) evaluated as {level}",
                    recommended_actions=["investigate"],
                    assigned_to="",  # placeholder
                    status="open",
                )
            )
    return alerts
