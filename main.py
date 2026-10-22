"""Forecast storage capacity; storage only, excluding compute/egress/requests."""
from decimal import Decimal as D


def forecast(daily_gb, retention_days, replicas, price_per_gb_month):
    values = [D(str(v)) for v in (daily_gb, retention_days, replicas, price_per_gb_month)]
    if any(not v.is_finite() or v < 0 for v in values) or values[2] < 1:
        raise ValueError('Invalid capacity parameters')
    stored = values[0] * values[1] * values[2]
    return {'steady_state_gb': str(stored), 'monthly_storage_only': str(stored*values[3])}


if __name__ == '__main__':
    print(forecast('0.4', 90, 2, '0.025'))
