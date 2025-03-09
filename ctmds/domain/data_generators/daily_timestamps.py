from datetime import datetime
from typing import cast

from pytz import country_timezones

from ctmds.domain.constants import CountryCodes, Granularity, TimePeriod
from ctmds.domain.data_generators.utils.date import TimezoneAwareDate


def format_time(
    input_hour: int,
    granularity: Granularity,
) -> TimePeriod:
    """Format time as HHMM"""
    granular_hour = input_hour if granularity == Granularity.HOURLY else input_hour // 2
    granular_minute = 0 if granularity == Granularity.HOURLY else (input_hour % 2) * 30
    return cast(TimePeriod, f"{granular_hour:02d}{granular_minute:02d}")


def daily_timestamps(
    date: datetime,
    country_code: CountryCodes,
    granularity: Granularity = Granularity.HALF_HOURLY,
) -> list[str]:
    """
    Generate timestamps for a specific country and date.

    Handles DST transitions:
    - Short days (23 hours) during spring forward
    - Long days (25 hours) during fall back
    - Normal days (24 hours)

    Args:
        date: The date to generate prices for
        country_code: The country code (GB, FR, NL, DE)
        granularity: Time granularity (hourly or half-hourly)

    Returns:
        List of timestamps
    """

    periods = get_day_periods(date, country_code, granularity)

    timestamps = list(map(lambda i: format_time(i, granularity), range(periods)))
    return timestamps


def get_day_periods(
    date: datetime,
    country_code: CountryCodes,
    granularity: Granularity = Granularity.HALF_HOURLY,
) -> int:
    """Get the last period for a specific country and date."""

    timezone = country_timezones[country_code.value][0]
    day_hours = TimezoneAwareDate(date, timezone).get_day_hours()

    # Calculate number of periods based on actual hours and granularity
    periods = day_hours * 2 if granularity == Granularity.HALF_HOURLY else day_hours

    return periods


def get_last_period(
    date: datetime,
    country_code: CountryCodes,
    granularity: Granularity = Granularity.HALF_HOURLY,
) -> TimePeriod:
    """Get the last period for a specific country and date."""

    periods = get_day_periods(date, country_code, granularity)
    last_period = format_time(periods, granularity)
    return last_period
