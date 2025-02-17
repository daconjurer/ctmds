import typer
from datetime import datetime
from typing import Type
from ctmds.domain.constants import CountryCodes, Granularity, SupportedCommodities
from ctmds.data_generators.raw_price import random_generator
from ctmds.domain import exceptions
from ctmds.domain.commodities.commodities_map import CommodityMap
from ctmds.domain.commodities.generators_map import GeneratorMap
from ctmds.domain.models.commodity.generic import GenericCommodity
from ctmds.domain.models.price_generator.generic import GenericDailyPricesGenerator
import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, level="INFO")

app = typer.Typer()


@app.command(name="random-prices")
def random_decimals(num: int):
    """Generate random decimal numbers using different methods"""
    random_generator(num)


@app.command(name="daily-prices")
def daily_prices(
    for_date: datetime = typer.Argument(
        ..., help="Date to generate prices for (YYYY-MM-DD)"
    ),
    country_code: CountryCodes = typer.Argument(
        default=CountryCodes.GB,
        help=f"Country code ({', '.join(code.value for code in CountryCodes)})",
    ),
    commodity: SupportedCommodities = typer.Argument(
        default=SupportedCommodities.CRUDE,
        help="Commodity to generate prices for",
    ),
    granularity: Granularity = typer.Option(
        default=Granularity.HOURLY,
        help="Time granularity (h: hourly, hh: half-hourly)",
    ),
    seed: int | None = typer.Option(
        default=None, metavar="--seed", help="Random seed for reproducibility"
    ),
):
    """Generate random daily prices for a specific country and date"""
    try:
        commodity_class: Type[GenericCommodity] = CommodityMap.get_commodity_class(commodity)
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

        # print(prices)
    except exceptions.IncorrectCountryCodeError as e:
        raise typer.BadParameter(e)


if __name__ == "__main__":
    app()
