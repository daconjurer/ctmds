from typing import Type

from ctmds.domain.commodities.crude import CrudeOil
from ctmds.domain.commodities.interface import CommodityInterface
from ctmds.domain.constants import SupportedCommodities


class CommodityMap:
    """Map of supported commodities to their implementations."""

    _commodity_map = {
        SupportedCommodities.CRUDE: CrudeOil,
    }

    @staticmethod
    def get_commodity(commodity: SupportedCommodities) -> Type[CommodityInterface]:
        """Get the commodity implementation for a given commodity."""
        return CommodityMap._commodity_map[commodity]
