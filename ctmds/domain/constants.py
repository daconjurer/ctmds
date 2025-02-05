from enum import Enum
from typing import Dict


class Granularity(str, Enum):
    HOURLY = "h"
    HALF_HOURLY = "hh"


class CountryCodes(str, Enum):
    GB = "GB"
    FR = "FR"
    NL = "NL"
    DE = "DE"


# Base prices for each country in EUR/MWh
COUNTRY_BASE_PRICES: Dict[CountryCodes, float] = {
    CountryCodes.GB: 61.0,
    CountryCodes.FR: 58.0,
    CountryCodes.NL: 52.0,
    CountryCodes.DE: 57.0,
}
