from datetime import datetime
from typing import Protocol

from ctmds.domain.commodity_price.models.price import PriceCollection
from ctmds.domain.constants import CountryCodes


class IDailyPricesGenerator(Protocol):
    """Protocol defining the interface for daily prices generators."""

    def get_daily_prices(
        self,
        date: datetime,
        country_code: CountryCodes,
    ) -> PriceCollection:
        """Generate daily prices for a given date and country code."""
        ...


class IPricesGenerator(Protocol):
    """Protocol for price generator functions."""

    def __call__(
        self,
        date: datetime,
    ) -> list[float]:
        """
        Generate prices for a commodity.

        Args:
            date: The date to generate prices for

        Returns:
            List of generated prices
        """
        ...
