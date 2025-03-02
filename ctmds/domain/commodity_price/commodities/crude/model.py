from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.entities import CrudeOilConfig


class CrudeOilConfigReader(GenericReader[CrudeOilConfig]):
    """Reader for CrudeOilConfig."""

    model = CrudeOilConfig


class CrudeOil(GenericCommodity):
    """Implementation of CommodityInterface for crude oil."""

    reader = CrudeOilConfigReader()
