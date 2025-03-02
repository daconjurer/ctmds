from datetime import datetime
from typing import Type

from ctmds.domain.commodity_price.commodities.commodities_map import CommodityMap
from ctmds.domain.commodity_price.commodities.generators_map import GeneratorMap
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.commodity_price.models.price import PriceCollection
from ctmds.domain.commodity_price.models.price_generator.generic import (
    GenericDailyPricesGenerator,
)
from ctmds.domain.constants import CountryCodes, Granularity, SupportedCommodities


def generate_daily_data(
    for_date: datetime,
    country_code: CountryCodes,
    commodity: SupportedCommodities,
    granularity: Granularity,
    seed: int | None = None,
) -> PriceCollection:
    commodity_class: Type[GenericCommodity] = CommodityMap.get_commodity_class(
        commodity
    )
    base_price = float(commodity_class().get_base_price(country_code))

    prices_generator: GenericDailyPricesGenerator = GeneratorMap.get_generator(
        commodity,
    )

    prices = prices_generator.get_daily_prices(
        date=for_date,
        base_price=base_price,
        country_code=country_code,
        granularity=granularity,
        seed=seed,
    )

    return prices
