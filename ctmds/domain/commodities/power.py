from typing import Dict

from ctmds.domain.commodity.generic import GenericCommodity
from ctmds.domain.constants import CountryCodes


class Power(GenericCommodity):
    """Implementation of CommodityInterface for power."""

    BASE_PRICES: Dict[CountryCodes, float] = {
        CountryCodes.GB: 108.50,  # GBP/MWh
        CountryCodes.FR: 130.58,  # EUR/MWh
        CountryCodes.NL: 130.58,  # EUR/MWh
        CountryCodes.DE: 130.58,  # EUR/MWh
    }
