from typing import Dict

from ctmds.domain.commodity.generic import GenericCommodity
from ctmds.domain.constants import CountryCodes


class CrudeOil(GenericCommodity):
    """Implementation of CommodityInterface for crude oil."""

    BASE_PRICES: Dict[CountryCodes, float] = {
        CountryCodes.GB: 57.37,  # GBP/Bbl
        CountryCodes.FR: 69.03,  # EUR/Bbl
        CountryCodes.NL: 69.03,  # EUR/Bbl
        CountryCodes.DE: 69.03,  # EUR/Bbl
    }
