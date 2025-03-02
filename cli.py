import typer
from datetime import datetime
from typing import Type
from ctmds.domain.constants import CountryCodes, Granularity, SupportedCommodities
from ctmds.data_generators.raw_price import random_generator
from ctmds.domain import exceptions
from ctmds.domain.commodity_price.commodities.commodities_map import CommodityMap
from ctmds.domain.commodity_price.commodities.generators_map import GeneratorMap
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.commodity_price.models.price_generator.generic import GenericDailyPricesGenerator
import sys
from ctmds.domain.commodity_price.daily_data import generate_daily_data

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
        _ = generate_daily_data(
            for_date=for_date,
            country_code=country_code,
            commodity=commodity,
            granularity=granularity,
            seed=seed,
        )

        # print(prices)
    except exceptions.IncorrectCountryCodeError as e:
        raise typer.BadParameter(e)


if __name__ == "__main__":
    app()
