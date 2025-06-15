from typing import List
from ..models import Alert

_fake_alerts: List[Alert] = []


def list_alerts() -> List[Alert]:
    return _fake_alerts
