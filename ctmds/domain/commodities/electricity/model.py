from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.entities import ElectricityConfig
from ctmds.domain.models.commodity.generic import GenericCommodity


class ElectricityConfigReader(GenericReader[ElectricityConfig]):
    """Reader for ElectricityConfig."""

    model = ElectricityConfig


class Electricity(GenericCommodity):
    """Implementation of CommodityInterface for electricity."""

    reader = ElectricityConfigReader()
