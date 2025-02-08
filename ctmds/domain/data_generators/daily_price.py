from datetime import datetime
from typing import Callable, Sequence

from pydantic import BaseModel

from ctmds.domain.constants import COUNTRY_BASE_PRICES, CountryCodes, Granularity
from ctmds.domain.data_generators.dates import TimezoneAwareDate
from ctmds.domain.data_generators.raw_price import normal_distribution_generator


class DailyPrice(BaseModel):
    price: float
    timestamp: str


class DailyPricesCollection(BaseModel):
    prices: Sequence[DailyPrice]


# Mapping of country codes to their timezone names
COUNTRY_TIMEZONES = {
    CountryCodes.GB: "Europe/London",
    CountryCodes.FR: "Europe/Paris",
    CountryCodes.NL: "Europe/Amsterdam",
    CountryCodes.DE: "Europe/Berlin",
}


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
    country_code: CountryCodes,
    granularity: Granularity = Granularity.HOURLY,
    seed: int | None = None,
    daily_prices_generator: Callable = normal_distribution_generator,
) -> DailyPricesCollection:
    """
    Generate random daily prices for a specific country and date.

    Handles DST transitions:
    - Short days (23 hours) during spring forward
    - Long days (25 hours) during fall back
    - Normal days (24 hours)

    Args:
        date: The date to generate prices for
        country_code: The country code (GB, FR, NL, DE)
        granularity: Time granularity (hourly or half-hourly)
        seed: Random seed for reproducibility
        daily_prices_generator: Function to generate the prices

    Returns:
        Collection of daily prices with timestamps
    """

    timezone = COUNTRY_TIMEZONES[country_code]
    day_hours = TimezoneAwareDate(date, timezone).get_day_hours()

    # Calculate number of periods based on actual hours and granularity
    num_hours = day_hours
    periods = num_hours * 2 if granularity == Granularity.HALF_HOURLY else num_hours

    base_price = COUNTRY_BASE_PRICES[country_code]
    prices = daily_prices_generator(base_price=base_price, periods=periods, seed=seed)

    prices_with_timestamps = []
    for i, price in enumerate(prices):
        time_str = format_time(i, granularity)
        prices_with_timestamps.append(DailyPrice(price=price, timestamp=time_str))

    return DailyPricesCollection(prices=prices_with_timestamps)
