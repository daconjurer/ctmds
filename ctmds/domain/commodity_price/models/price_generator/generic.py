from datetime import datetime
from typing import Callable

from ctmds.domain.commodity_price.models.price import PriceCollection
from ctmds.domain.commodity_price.models.price_generator.interface import (
    DailyPricesGeneratorInterface,
    PriceGenerator,
)
from ctmds.domain.constants import CountryCodes, Granularity
from ctmds.domain.data_generators.daily_price import daily_prices_with_timestamps


class GenericDailyPricesGenerator(DailyPricesGeneratorInterface):
    """Generic daily prices generator."""

    def __init__(self, prices_generator: PriceGenerator):
        self.prices_generator: PriceGenerator = prices_generator
        self.daily_prices_with_timestamps_generator: Callable = (
            daily_prices_with_timestamps
        )

    def get_daily_prices(
        self,
        date: datetime,
        base_price: float,
        country_code: CountryCodes,
        granularity: Granularity,
        seed: int | None = None,
    ) -> PriceCollection:
        """Get daily generic commodity prices."""
        return self.daily_prices_with_timestamps_generator(
            date=date,
            base_price=base_price,
            country_code=country_code,
            granularity=granularity,
            seed=seed,
            daily_prices_generator=self.prices_generator,
        )
