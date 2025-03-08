from decimal import Decimal
from typing import Protocol

from ctmds.domain.constants import CountryCodes, TimePeriod


class ICommodity(Protocol):
    """Protocol defining the interface for commodities."""

    def get_price(
        self,
        country_code: CountryCodes,
        period: TimePeriod,
    ) -> Decimal:
        """Get base price for the commodity in a country."""
        ...

    def get_supported_countries(self) -> list[CountryCodes]:
        """Get list of supported country codes."""
        ...
