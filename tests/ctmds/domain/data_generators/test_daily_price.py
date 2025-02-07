from datetime import datetime

import pytest

from ctmds.domain import exceptions
from ctmds.domain.constants import CountryCodes, Granularity
from ctmds.domain.data_generators.daily_price import daily_prices_with_timestamps


def test_daily_prices_with_timestamps_hourly():
    # Setup
    country_code = CountryCodes.GB
    for_date = datetime.now()
    granularity = Granularity.HOURLY
    seed = 123

    # Test
    result = daily_prices_with_timestamps(for_date, country_code, granularity, seed)

    # Validation
    assert len(result.prices) == 24
    assert all(isinstance(x.price, float) for x in result.prices)
    assert all(0 <= x.price < 100 for x in result.prices)

    # Check that the timestamps are in the correct format
    assert all(len(x.timestamp) == 4 for x in result.prices)
    assert all(x.timestamp.isdigit() for x in result.prices)


def test_daily_prices_with_timestamps_half_hourly():
    # Setup
    country_code = CountryCodes.GB
    for_date = datetime.now()
    granularity = Granularity.HALF_HOURLY
    seed = 123

    # Test
    result = daily_prices_with_timestamps(for_date, country_code, granularity, seed)

    # Validation
    assert len(result.prices) == 48
    assert all(isinstance(x.price, float) for x in result.prices)
    assert all(0 <= x.price < 100 for x in result.prices)

    # Check that the timestamps are in the correct format
    assert all(len(x.timestamp) == 4 for x in result.prices)
    assert all(x.timestamp.isdigit() for x in result.prices)


def test_daily_prices_with_timestamps_invalid_country_code():
    # Setup
    country_code = "ZZ"
    for_date = datetime.now()
    granularity = Granularity.HOURLY
    seed = 123

    # Test
    with pytest.raises(exceptions.IncorrectCountryCodeError):
        daily_prices_with_timestamps(for_date, country_code, granularity, seed)
