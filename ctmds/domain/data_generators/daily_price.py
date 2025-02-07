from datetime import datetime
from typing import Callable, Sequence

from pydantic import BaseModel

from ctmds.domain import exceptions
from ctmds.domain.constants import COUNTRY_BASE_PRICES, Granularity
from ctmds.domain.data_generators.raw_price import normal_distribution_generator


class DailyPrice(BaseModel):
    price: float
    timestamp: str


class DailyPricesCollection(BaseModel):
    prices: Sequence[DailyPrice]


def format_time(
    input_hour: int,
    granularity: Granularity,
) -> str:
    """Format time as HHMM"""
    granular_hour = input_hour if granularity == Granularity.HOURLY else input_hour // 2
    granular_minute = 0 if granularity == Granularity.HOURLY else (input_hour % 2) * 30
    return f"{granular_hour:02d}{granular_minute:02d}"


def daily_prices_with_timestamps(
    date: datetime,
    country_code: str,
    granularity: Granularity = Granularity.HOURLY,
    seed: int | None = None,
    daily_prices_generator: Callable = normal_distribution_generator,
) -> DailyPricesCollection:
    """Generate random daily prices for a specific country and date"""
    prices_with_timestamps = []

    if country_code not in COUNTRY_BASE_PRICES:
        raise exceptions.IncorrectCountryCodeError(
            f"Country code must be one of: {', '.join(COUNTRY_BASE_PRICES.keys())}"
        )

    base_price = COUNTRY_BASE_PRICES[country_code]
    periods = 48 if granularity == Granularity.HALF_HOURLY else 24

    prices = daily_prices_generator(base_price=base_price, periods=periods, seed=seed)

    for i, price in enumerate(prices):
        time_str = format_time(i, granularity)
        prices_with_timestamps.append(DailyPrice(price=price, timestamp=time_str))

    return DailyPricesCollection(prices=prices_with_timestamps)
