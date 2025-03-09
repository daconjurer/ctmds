from datetime import datetime

from ctmds.domain.commodity_price.commodities.generators_map import GeneratorMap
from ctmds.domain.commodity_price.models.price import PriceCollection
from ctmds.domain.constants import CountryCodes, Granularity, SupportedCommodities


class DailyData:
    def __init__(
        self,
        for_date: datetime,
        country_code: CountryCodes,
        commodity: SupportedCommodities,
        granularity: Granularity,
        seed: int | None = None,
    ):
        self.for_date = for_date
        self.country_code = country_code
        self.commodity = commodity
        self.granularity = granularity
        self.seed = seed

    def _get_existing_data(self) -> PriceCollection | None:
        """Get existing data from the DB."""
        ...

    def _resample_prices(
        self,
        prices_collection: PriceCollection,
        granularity: Granularity,
    ) -> PriceCollection:
        """Resample prices to the specified granularity."""
        if granularity == Granularity.HALF_HOURLY:
            return prices_collection

        resampled_prices = prices_collection.prices[::2]
        return PriceCollection(prices=resampled_prices)

    def generate(self) -> PriceCollection:
        """Generate daily prices for a commodity."""

        # TODO: Hit the DB to check if the data already exists
        prices_collection = self._get_existing_data()

        # If it does not exist, generate new data
        if not prices_collection:
            prices_generator = GeneratorMap.get_generator(
                self.commodity,
                self.country_code,
            )

            prices_collection = prices_generator().get_daily_prices(
                date=self.for_date,
                country_code=self.country_code,
            )

            # And save it to the DB
            ...

        # Finally, return it with the specified granularity
        final_prices = self._resample_prices(prices_collection, self.granularity)

        return final_prices
