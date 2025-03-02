from ctmds.core.service.generic import GenericService
from ctmds.core.utils.filter_sort import SortParams
from ctmds.domain.entities import ExchangeRate
from ctmds.domain.exchange_rate.reader import (
    ExchangeRateFilterParams,
    exchange_rate_reader,
)


class ExchangeRateService(GenericService[ExchangeRate]):
    reader = exchange_rate_reader

    def get_current_exchange_rate(
        self,
        filter: ExchangeRateFilterParams,
        sort: SortParams,
    ) -> ExchangeRate | None:
        result = self.reader.get_many(
            db=next(self.db()),
            filter=filter,
            sort=sort,
            limit=1,
        )

        if result:
            return result[0]

        return None
