from typing import Callable, Dict

from ctmds.data_generators.raw_price import normal_distribution_generator
from ctmds.domain.commodity.generic import GenericCommodity
from ctmds.domain.constants import CountryCodes


class NaturalGas(GenericCommodity):
    """Implementation of CommodityInterface for natural gas."""

    prices_generator: Callable = normal_distribution_generator

    BASE_PRICES: Dict[CountryCodes, float] = {
        CountryCodes.GB: 2.67,  # GBP/MMBtu
        CountryCodes.FR: 3.21,  # EUR/MMBtu
        CountryCodes.NL: 3.21,  # EUR/MMBtu
        CountryCodes.DE: 3.21,  # EUR/MMBtu
    }
