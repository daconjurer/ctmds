from datetime import datetime
from typing import List, Optional, Protocol

from ctmds.domain.constants import CountryCodes, Granularity
from ctmds.domain.models.price import PriceCollection


class CommodityInterface(Protocol):
    """Protocol defining the interface for commodities."""

    def get_daily_prices(
        self,
        date: datetime,
        country_code: CountryCodes,
        granularity: Granularity,
        seed: Optional[int] = None,
    ) -> PriceCollection:
        """
        Get daily prices for the commodity.

        Args:
            date: The date to get prices for
            country_code: The country code (e.g., 'GB', 'FR')
            seed: Optional random seed for reproducibility

        Returns:
            Collection of daily prices with timestamps

        Raises:
            IncorrectCountryCodeError: If country_code is not supported
        """
        ...

    def get_base_price(self, country_code: CountryCodes) -> float:
        """
        Get the base price for a country.

        Args:
            country_code: The country code

        Returns:
            Base price for the commodity in the specified country

        Raises:
            IncorrectCountryCodeError: If country_code is not supported
        """
        ...

    def get_supported_countries(self) -> List[CountryCodes]:
        """
        Get list of supported country codes.

        Returns:
            List of supported country codes
        """
        ...

    def validate_country_code(self, country_code: CountryCodes) -> None:
        """
        Validate if a country code is supported.

        Args:
            country_code: The country code to validate

        Raises:
            IncorrectCountryCodeError: If country_code is not supported
        """
        ...
