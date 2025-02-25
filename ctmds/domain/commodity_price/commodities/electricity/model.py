from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.entities import ElectricityConfig


class ElectricityConfigReader(GenericReader[ElectricityConfig]):
    """Reader for ElectricityConfig."""

    model = ElectricityConfig


class Electricity(GenericCommodity):
    """Implementation of CommodityInterface for electricity."""

    reader = ElectricityConfigReader()
