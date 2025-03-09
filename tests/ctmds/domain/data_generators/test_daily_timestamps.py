from datetime import datetime

import pytest

from ctmds.domain.constants import CountryCodes, Granularity
from ctmds.domain.data_generators.daily_timestamps import daily_timestamps


def test_daily_timestamps_hourly():
    # Setup
    country_code = CountryCodes.GB
    for_date = datetime.now()
    granularity = Granularity.HOURLY

    # Test
    result = daily_timestamps(
        date=for_date,
        country_code=country_code,
        granularity=granularity,
    )

    # Validation
    assert len(result) == 24
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 4 for x in result)
    assert all(x.isdigit() for x in result)


def test_daily_timestamps_half_hourly():
    # Setup
    country_code = CountryCodes.GB
    for_date = datetime.now()
    granularity = Granularity.HALF_HOURLY

    # Test
    result = daily_timestamps(
        date=for_date,
        country_code=country_code,
        granularity=granularity,
    )

    # Validation
    assert len(result) == 48
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 4 for x in result)
    assert all(x.isdigit() for x in result)


@pytest.mark.parametrize(
    "country_code,dst_dates",
    [
        (
            CountryCodes.GB,
            {
                "short_day": "2024-03-31",  # British Summer Time starts
                "long_day": "2024-10-27",  # British Summer Time ends
                "normal_day": "2024-06-15",
            },
        ),
        (
            CountryCodes.FR,
            {
                "short_day": "2024-03-31",  # Central European Summer Time starts
                "long_day": "2024-10-27",  # Central European Summer Time ends
                "normal_day": "2024-06-15",
            },
        ),
        (
            CountryCodes.NL,
            {
                "short_day": "2024-03-31",  # Central European Summer Time starts
                "long_day": "2024-10-27",  # Central European Summer Time ends
                "normal_day": "2024-06-15",
            },
        ),
        (
            CountryCodes.DE,
            {
                "short_day": "2024-03-31",  # Central European Summer Time starts
                "long_day": "2024-10-27",  # Central European Summer Time ends
                "normal_day": "2024-06-15",
            },
        ),
    ],
)
def test_dst_transitions(country_code: CountryCodes, dst_dates: dict[str, str]):
    # Test short day (spring forward)
    short_day = datetime.strptime(dst_dates["short_day"], "%Y-%m-%d")
    result = daily_timestamps(
        date=short_day,
        country_code=country_code,
        granularity=Granularity.HOURLY,
    )
    assert len(result) == 23, "DST start should have 23 hours"

    # Test long day (fall back)
    long_day = datetime.strptime(dst_dates["long_day"], "%Y-%m-%d")
    result = daily_timestamps(
        date=long_day,
        country_code=country_code,
        granularity=Granularity.HOURLY,
    )
    assert len(result) == 25, "DST end should have 25 hours"

    # Test normal day
    normal_day = datetime.strptime(dst_dates["normal_day"], "%Y-%m-%d")
    result = daily_timestamps(
        date=normal_day,
        country_code=country_code,
        granularity=Granularity.HOURLY,
    )
    assert len(result) == 24, "Normal day should have 24 hours"


def test_half_hourly_dst_transitions():
    # Test half-hourly granularity during DST transition
    date = datetime.strptime("2024-03-31", "%Y-%m-%d")  # BST starts
    result = daily_timestamps(
        date=date,
        country_code=CountryCodes.GB,
        granularity=Granularity.HALF_HOURLY,
    )
    assert len(result) == 46, "Short day should have 46 half-hour periods"


def test_timestamp_format():
    date = datetime.strptime("2024-06-15", "%Y-%m-%d")
    result = daily_timestamps(
        date=date,
        country_code=CountryCodes.GB,
        granularity=Granularity.HOURLY,
    )

    # Check first and last timestamps
    assert result[0] == "0000"
    assert result[-1] == "2300"
