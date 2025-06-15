from typing import List, Optional
from enum import Enum
from uuid import UUID
from datetime import datetime, timedelta
from pydantic import BaseModel


class Thresholds(BaseModel):
    low: float
    medium: float
    high: float
    critical: float


class RiskIndicator(BaseModel):
    id: UUID
    name: str
    category: str
    description: Optional[str] = None
    calculation_method: str
    data_sources: List[str]
    thresholds: Thresholds
    weight: float
    update_frequency: timedelta
    owner: str


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class AlertSeverity(str, Enum):
    info = "info"
    warning = "warning"
    critical = "critical"


class RiskSnapshot(BaseModel):
    timestamp: datetime
    indicator_id: UUID
    value: float
    normalized_score: float
    risk_level: RiskLevel
    trend: str
    confidence: float


class Alert(BaseModel):
    id: UUID
    indicator_id: UUID
    triggered_at: datetime
    severity: AlertSeverity
    title: str
    description: str
    recommended_actions: List[str]
    assigned_to: str
    status: str
    resolution_notes: Optional[str] = None
