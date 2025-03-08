from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.entities import CommodityConfig, CrudeOilConfig


class CrudeOilConfigReader(GenericReader[CommodityConfig]):
    """Reader for CrudeOilConfig."""

    model = CrudeOilConfig


class CrudeOil(GenericCommodity):
    """Implementation of ICommodity for crude oil."""

    reader = CrudeOilConfigReader()
