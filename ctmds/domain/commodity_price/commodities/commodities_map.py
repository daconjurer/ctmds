from typing import Type

from ctmds.domain.commodity_price.commodities.crude.model import CrudeOil
from ctmds.domain.commodity_price.commodities.electricity.model import Electricity
from ctmds.domain.commodity_price.commodities.natural_gas.model import NaturalGas
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.constants import SupportedCommodities


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
    ) -> Type[GenericCommodity]:
        """Get the commodity implementation for a given commodity."""
        return CommodityMap._commodity_map.get(commodity, CrudeOil)
