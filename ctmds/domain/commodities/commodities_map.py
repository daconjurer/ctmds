from typing import Type

from ctmds.domain.commodities.crude.model import CrudeOil
from ctmds.domain.commodities.electricity.model import Electricity
from ctmds.domain.commodities.natural_gas.model import NaturalGas
from ctmds.domain.constants import SupportedCommodities
from ctmds.domain.models.commodity.interface import CommodityInterface


class CommodityMap:
    """Map of supported commodities to their implementations."""

    _commodity_map = {
        SupportedCommodities.CRUDE: CrudeOil,
        SupportedCommodities.NATURAL_GAS: NaturalGas,
        SupportedCommodities.POWER: Electricity,
    }

    @staticmethod
    def get_commodity_class(
        commodity: SupportedCommodities,
    ) -> Type[CommodityInterface]:
        """Get the commodity implementation for a given commodity."""
        return CommodityMap._commodity_map.get(commodity, CrudeOil)
