from pydantic import Field

from ctmds.core.data_access.reader import GenericReader
from ctmds.core.utils.filter_sort import BaseFilterParams
from ctmds.domain.entities import ExchangeRate


class ExchangeRateFilterParams(BaseFilterParams):
    from_currency: str | None = Field(
        default=None,
        examples=["USD"],
        description="Source currency of the exchange rate",
    )
    to_currency: str | None = Field(
        default=None,
        examples=["EUR"],
        description="Target currency of the exchange rate",
    )


class ExchangeRateReader(GenericReader[ExchangeRate]):
    model = ExchangeRate


exchange_rate_reader = ExchangeRateReader()
