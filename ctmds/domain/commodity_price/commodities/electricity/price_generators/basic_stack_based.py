from datetime import datetime

from ctmds.domain.commodity_price.commodities.electricity.generation_stack.demand_profile import (
    generate_demand_profile,
)
from ctmds.domain.commodity_price.commodities.electricity.generation_stack.interfaces import (
    IDemandProfileGenerator,
)
from ctmds.domain.commodity_price.commodities.electricity.price_generators.stacks import (
    StackMap,
)
from ctmds.domain.constants import CountryCodes
from ctmds.domain.data_generators.daily_timestamps import get_day_periods


def stack_generation_based_price_generator(
    country_code: CountryCodes,
    date: datetime,
    demand_profile: IDemandProfileGenerator = generate_demand_profile,
    seed: int | None = None,
) -> list[float]:
    """
    Generate power prices using a merit-order based generation stack.

    Args:
        country_code: Country code to use for price calculation
        demand_profile: Function to generate demand profile
        date: Date to generate prices for
        seed: Random seed for reproducibility

    Returns:
        List of prices in currency/MWh
    """
    base_demand = 25.0
    peak_demand = 40.0

    stack = StackMap.get_stack(country_code)
    periods = get_day_periods(date, country_code)

    # Generate demand profile
    demands = demand_profile(
        periods=periods,
        date=date,
        base_demand=base_demand,
        peak_demand=peak_demand,
        seed=seed,
    )

    # Calculate prices based on demand
    prices = [stack.get_price_for_demand(demand) for demand in demands]

    # for demand, price in zip(demands, prices):
    #     print(f"{demand:.2f} GW -> {price:.2f} GBP/MWh")

    return prices
