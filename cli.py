import typer
from datetime import datetime
from ctmds.domain.constants import CountryCodes, Granularity, SupportedCommodities
from ctmds.domain.data_generators.raw_price import random_generator
from ctmds.domain import exceptions
import sys
from ctmds.domain.commodity_price.daily_data import DailyData

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
        default=SupportedCommodities.POWER,
        help="Commodity to generate prices for",
    ),
    granularity: Granularity = typer.Option(
        default=Granularity.HOURLY,
        help="Time granularity (h: hourly, hh: half-hourly)",
    ),
):
    """Generate random daily prices for a specific country and date"""
    try:
        prices = DailyData(
            for_date=for_date,
            country_code=country_code,
            commodity=commodity,
            granularity=granularity,
        ).generate()

        # print(prices)
    except exceptions.IncorrectCountryCodeError as e:
        raise typer.BadParameter(e)


if __name__ == "__main__":
    app()
