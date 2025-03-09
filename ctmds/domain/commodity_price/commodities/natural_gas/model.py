from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.entities import CommodityConfig, NaturalGasConfig


class NaturalGasConfigReader(GenericReader[CommodityConfig]):
    """Reader for NaturalGasConfig."""

    model = NaturalGasConfig


class NaturalGas(GenericCommodity):
    """Implementation of ICommodity for natural gas."""

    reader = NaturalGasConfigReader()
