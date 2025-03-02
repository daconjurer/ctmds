from datetime import datetime

from pydantic import BaseModel

from ctmds.domain.constants import CountryCodes, Granularity, SupportedCommodities


class DailyDataRequest(BaseModel):
    for_date: datetime
    country_code: CountryCodes
    commodity: SupportedCommodities
    granularity: Granularity
    seed: int | None = None
