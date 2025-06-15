from uuid import UUID
from datetime import timedelta
from .models import RiskIndicator, Thresholds

SAMPLE_INDICATORS = [
    RiskIndicator(
        id=UUID('11111111-1111-1111-1111-111111111111'),
        name='System Availability',
        category='Operational Risk',
        description='Percentage of time the system is available',
        calculation_method='raw_percentage',
        data_sources=['monitoring'],
        thresholds=Thresholds(low=90, medium=95, high=99, critical=99.9),
        weight=0.2,
        update_frequency=timedelta(minutes=5),
        owner='ops-team',
    ),
    RiskIndicator(
        id=UUID('22222222-2222-2222-2222-222222222222'),
        name='Revenue Variance',
        category='Financial Risk',
        description='Difference between expected and actual revenue',
        calculation_method='percentage_variance',
        data_sources=['finance-system'],
        thresholds=Thresholds(low=5, medium=10, high=20, critical=30),
        weight=0.3,
        update_frequency=timedelta(hours=1),
        owner='finance-team',
    ),
]
