from datetime import datetime
from typing import List, Protocol

from ctmds.domain.commodity_price.models.price import PriceCollection
from ctmds.domain.constants import CountryCodes, Granularity


class IDailyPricesGenerator(Protocol):
    """Protocol defining the interface for daily prices generators."""

    def get_daily_prices(
        self,
        date: datetime,
        base_price: float,
        country_code: CountryCodes,
        granularity: Granularity,
        seed: int | None = None,
    ) -> PriceCollection:
        """Generate daily prices for a given date and country code."""
        ...


class IPricesGenerator(Protocol):
    """Protocol for price generator functions."""

    def __call__(
        self,
        base_price: float,
        periods: int,
        date: datetime,
        seed: int | None = None,
        volatility: float = ...,  # Default value varies by generator
    ) -> List[float]:
        """
        Generate prices for a commodity.

        Args:
            base_price: Base price for the commodity
            periods: Number of periods to generate prices for
            date: The date to generate prices for
            seed: Optional random seed for reproducibility
            volatility: Base volatility level (defaults vary by commodity)

        Returns:
            List of generated prices
        """
        ...
