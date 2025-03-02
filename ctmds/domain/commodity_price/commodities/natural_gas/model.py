from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.entities import NaturalGasConfig


class NaturalGasConfigReader(GenericReader[NaturalGasConfig]):
    """Reader for NaturalGasConfig."""

    model = NaturalGasConfig


class NaturalGas(GenericCommodity):
    """Implementation of CommodityInterface for natural gas."""

    reader = NaturalGasConfigReader()
