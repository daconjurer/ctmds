from enum import Enum
from typing import Literal


class Granularity(str, Enum):
    HOURLY = "h"
    HALF_HOURLY = "hh"


class CountryCodes(str, Enum):
    GB = "GB"
    FR = "FR"
    NL = "NL"
    DE = "DE"


class SupportedCommodities(str, Enum):
    CRUDE = "crude"
    NATURAL_GAS = "natgas"
    POWER = "power"


TimePeriod = Literal[
    "0000",
    "0030",
    "0100",
    "0130",
    "0200",
    "0230",
    "0300",
    "0330",
    "0400",
    "0430",
    "0500",
    "0530",
    "0600",
    "0630",
    "0700",
    "0730",
    "0800",
    "0830",
    "0900",
    "0930",
    "1000",
    "1030",
    "1100",
    "1130",
    "1200",
    "1230",
    "1300",
    "1330",
    "1400",
    "1430",
    "1500",
    "1530",
    "1600",
    "1630",
    "1700",
    "1730",
    "1800",
    "1830",
    "1900",
    "1930",
    "2000",
    "2030",
    "2100",
    "2130",
    "2200",
    "2230",
    "2300",
    "2330",
    "2400",
    "2430",
]
