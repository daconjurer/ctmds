from datetime import datetime

import numpy as np


def generate_demand_profile(
    periods: int,
    date: datetime,
    base_demand: float = 25.0,  # GW
    peak_demand: float = 40.0,  # GW
    seed: int | None = None,
) -> list[float]:
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
