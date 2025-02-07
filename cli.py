import typer
from datetime import datetime

from ctmds.domain.data_generators.daily_price import (
    daily_prices_with_timestamps,
    Granularity,
)
from ctmds.domain.constants import CountryCodes
from ctmds.domain.data_generators.raw_price import random_generator
from ctmds.domain import exceptions

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
        daily_prices_with_timestamps(for_date, country_code, granularity, seed)
    except exceptions.IncorrectCountryCodeError as e:
        raise typer.BadParameter(e)


if __name__ == "__main__":
    app()
