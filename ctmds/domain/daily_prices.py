from datetime import datetime
from typing import Callable

from ctmds.domain import exceptions
from ctmds.domain.constants import COUNTRY_BASE_PRICES, Granularity
from ctmds.domain.price_generators import normal_distribution_generator


def format_time(
    input_hour: int,
    granularity: Granularity,
) -> str:
    """Format time as HHMM"""
    granular_hour = input_hour if granularity == Granularity.HOURLY else input_hour // 2
    granular_minute = 0 if granularity == Granularity.HOURLY else (input_hour % 2) * 30
    return f"{granular_hour:02d}{granular_minute:02d}"


def generate_daily_prices_with_timestamps(
    for_date: datetime,
    country_code: str,
    granularity: Granularity = Granularity.HOURLY,
    seed: int | None = None,
    daily_prices_generator: Callable = normal_distribution_generator,
):
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
        prices_with_timestamps.append((time_str, price))

    # Print results
    print(f"Daily prices for {country_code} on {for_date}")
    print(f"Base price: £{COUNTRY_BASE_PRICES[country_code]:.2f}/MWh")
    print("-" * 30)

    for timestamp, price in prices_with_timestamps:
        print(f"{timestamp}: £{price:.2f}")
