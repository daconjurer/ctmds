from datetime import datetime

from ctmds.core.data_access.interfaces import Schema


class ExchangeRateCreate(Schema):
    from_currency: str
    to_currency: str
    rate: float
    effective_date: datetime


class ExchangeRatePublic(Schema):
    from_currency: str
    to_currency: str
    rate: float
    effective_date: datetime
