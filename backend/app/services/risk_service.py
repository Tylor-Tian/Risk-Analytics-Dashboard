from typing import List
from ..models import RiskIndicator


# Temporary in-memory data store
_fake_indicators: List[RiskIndicator] = []


def list_indicators() -> List[RiskIndicator]:
    return _fake_indicators


def add_indicator(indicator: RiskIndicator) -> None:
    _fake_indicators.append(indicator)
