from datetime import datetime

from ctmds.domain.commodity_price.models.price import Price, PriceCollection
from ctmds.domain.commodity_price.models.price_generator.interface import (
    IDailyPricesGenerator,
    IPricesGenerator,
)
from ctmds.domain.constants import CountryCodes, Granularity
from ctmds.domain.data_generators.daily_timestamps import daily_timestamps


class GenericDailyPricesGenerator(IDailyPricesGenerator):
    """Generic daily prices generator."""

    def __init__(self, prices_generator: IPricesGenerator):
        self.prices_generator: IPricesGenerator = prices_generator

    def get_daily_prices(
        self,
        date: datetime,
        country_code: CountryCodes,
        granularity: Granularity = Granularity.HALF_HOURLY,
    ) -> PriceCollection:
        """Get daily generic commodity prices."""

        # First get timestamps
        timestamps = daily_timestamps(date, country_code)
        # From the number of timestamps we get periods, and from those + date we get prices
        prices = self.prices_generator(date=date)

        prices_with_timestamps = [
            Price(price=price, timestamp=timestamp)
            for price, timestamp in zip(prices, timestamps)
        ]

        return PriceCollection(
            prices=prices_with_timestamps,
        )
