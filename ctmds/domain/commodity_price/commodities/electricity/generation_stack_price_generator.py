from datetime import datetime
from typing import List, Sequence

import numpy as np

from ctmds.domain.commodity_price.commodities.electricity.generation.generators import (
    GasElectricityGenerator,
    NuclearElectricityGenerator,
    PeakElectricityGenerator,
    SolarElectricityGenerator,
    WindElectricityGenerator,
)
from ctmds.domain.commodity_price.commodities.electricity.generation.generic import (
    GenericElectricityGenerator,
)


class GenerationStack:
    """Represents a merit-order based generation stack."""

    def __init__(self, generators: Sequence[GenericElectricityGenerator]):
        """
        Initialize generation stack with ordered generators.

        Args:
            generators: List of generators, will be ordered by marginal cost
        """
        # Sort generators by marginal cost (merit order)
        self.generators = sorted(generators, key=lambda g: g.marginal_cost)
        self.total_capacity = sum(gen.capacity for gen in self.generators)

    def get_price_for_demand(self, demand: float) -> float:
        """
        Get the marginal price for a given demand level.

        Args:
            demand: Total demand in GW

        Returns:
            Marginal price in currency/MWh
        """
        if demand <= 0:
            return 0.0

        if demand > self.total_capacity:
            # If demand exceeds total capacity, return highest marginal cost with scarcity premium
            return self.generators[-1].marginal_cost * 1.5

        remaining_demand = demand
        marginal_price = 0.0

        for generator in self.generators:
            if remaining_demand <= 0:
                break

            # How much of this generator's capacity is used
            used_capacity = min(generator.capacity, remaining_demand)

            if used_capacity > 0:
                # Update marginal price if this generator is used
                marginal_price = generator.marginal_cost

            remaining_demand -= used_capacity

        return marginal_price


def generate_demand_profile(
    periods: int,
    date: datetime,
    base_demand: float = 25.0,  # GW
    peak_demand: float = 40.0,  # GW
    seed: int | None = None,
) -> List[float]:
    """
    Generate a daily demand profile.

    Args:
        periods: Number of periods to generate
        date: Date for the demand profile
        base_demand: Minimum demand level
        peak_demand: Maximum demand level
        seed: Random seed for reproducibility

    Returns:
        List of demand values in GW
    """
    if seed is not None:
        np.random.seed(seed)

    # Create time-based pattern
    hour_factors = {
        0: 0.7,
        1: 0.65,
        2: 0.6,
        3: 0.6,  # Night (low demand)
        4: 0.7,
        5: 0.8,
        6: 1.0,
        7: 1.3,  # Morning ramp
        8: 1.4,
        9: 1.3,
        10: 1.2,
        11: 1.1,  # Morning peak
        12: 1.0,
        13: 0.9,
        14: 0.9,
        15: 0.95,  # Afternoon
        16: 1.1,
        17: 1.4,
        18: 1.5,
        19: 1.4,  # Evening peak
        20: 1.2,
        21: 1.0,
        22: 0.9,
        23: 0.8,  # Evening decline
    }

    # Weekend adjustment
    weekend_factor = 0.8 if date.weekday() >= 5 else 1.0

    demands = []
    demand_range = peak_demand - base_demand

    for i in range(periods):
        hour = i % 24
        hour_factor = hour_factors[hour]

        # Base pattern
        demand = base_demand + (demand_range * hour_factor * weekend_factor)

        # Add random noise (±5%)
        noise = np.random.uniform(-0.05, 0.05) * demand
        demand = max(base_demand, demand + noise)

        demands.append(demand)

    return demands


def power_price_generator(
    periods: int,
    date: datetime,
    seed: int | None = None,
) -> List[float]:
    """
    Generate power prices using a merit-order based generation stack.

    Args:
        periods: Number of periods to generate prices for
        date: Date to generate prices for
        seed: Random seed for reproducibility

    Returns:
        List of prices in currency/MWh
    """
    # Create generation stack with default generators
    stack = GenerationStack(
        [
            SolarElectricityGenerator(),
            WindElectricityGenerator(),
            NuclearElectricityGenerator(),
            GasElectricityGenerator(),
            PeakElectricityGenerator(),
        ]
    )

    # Generate demand profile
    demands = generate_demand_profile(periods, date, seed=seed)

    # Calculate prices based on demand
    prices = [stack.get_price_for_demand(demand) for demand in demands]

    for demand, price in zip(demands, prices):
        print(f"{demand:.2f} GW -> {price:.2f} GBP/MWh")

    return prices
