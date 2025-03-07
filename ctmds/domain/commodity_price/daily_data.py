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

    def generate(self) -> PriceCollection:
        prices_generator = GeneratorMap.get_generator(self.commodity)

        prices = prices_generator().get_daily_prices(
            date=self.for_date,
            country_code=self.country_code,
        )

        return prices
