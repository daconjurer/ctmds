from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.entities import CrudeOilConfig
from ctmds.domain.models.commodity.generic import GenericCommodity


class CrudeOilConfigReader(GenericReader[CrudeOilConfig]):
    """Reader for CrudeOilConfig."""

    model = CrudeOilConfig


class CrudeOil(GenericCommodity):
    """Implementation of CommodityInterface for crude oil."""

    reader = CrudeOilConfigReader()
