from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.entities import CommodityConfig, ElectricityConfig


class ElectricityConfigReader(GenericReader[CommodityConfig]):
    """Reader for ElectricityConfig."""

    model = ElectricityConfig


class Electricity(GenericCommodity):
    """Implementation of ICommodity for electricity."""

    reader = ElectricityConfigReader()
