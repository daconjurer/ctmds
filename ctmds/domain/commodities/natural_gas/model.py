from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.entities import NaturalGasConfig
from ctmds.domain.models.commodity.generic import GenericCommodity


class NaturalGasConfigReader(GenericReader[NaturalGasConfig]):
    """Reader for NaturalGasConfig."""

    model = NaturalGasConfig


class NaturalGas(GenericCommodity):
    """Implementation of CommodityInterface for natural gas."""

    reader = NaturalGasConfigReader()
