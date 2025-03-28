from decimal import Decimal
from typing import cast

from ctmds.core.data_access.reader import GenericReader
from ctmds.core.db.session import SessionStream, get_session
from ctmds.core.utils.filter_sort import BaseFilterParams
from ctmds.domain import exceptions
from ctmds.domain.commodity_price.models.commodity.interface import ICommodity
from ctmds.domain.constants import CountryCodes, TimePeriod
from ctmds.domain.entities import CommodityConfig


class GenericCommodityFilterParams(BaseFilterParams):
    country_code: CountryCodes


class GenericCommodity(ICommodity):
    """Implementation of ICommodity for generic commodity."""

    reader: GenericReader[CommodityConfig]

    def __init__(self):
        self.session_stream: SessionStream = get_session

    def get_price(
        self,
        country_code: CountryCodes,
        period: TimePeriod,
    ) -> Decimal:
        """Get current price for generic commodity in a country, if valid."""

        # TODO: Get price for "period" from database table with daily prices

        valid_country_code = self.reader.get_by(
            db=next(self.session_stream()),
            filter=GenericCommodityFilterParams(country_code=country_code),
        )

        if not valid_country_code:
            raise exceptions.IncorrectCountryCodeError(
                f"Country code must be one of: {', '.join(self.get_supported_countries())}"
            )

        base_price = cast(Decimal, valid_country_code.base_price)
        return base_price

    def get_supported_countries(self) -> list[CountryCodes]:
        """Get list of supported country codes."""
        result = []
        page = 1
        limit = 10
        batch_length = 10

        while batch_length == limit:
            batch_result = self.reader.get_many(
                db=next(self.session_stream()),
                page=page,
                limit=limit,
            )
            result.extend(batch_result)
            batch_length = len(batch_result)
            page += 1

        return [commodity_config.country_code for commodity_config in result]
