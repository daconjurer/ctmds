import numpy as np


def normal_distribution_generator(
    base_price: float,
    periods: int,
    std_dev: float = 2.0,
    seed: int | None = None,
) -> list[float]:
    """Generate random decimals representing prices, following a normal distribution"""
    if seed is not None:
        np.random.seed(seed)
    return list(np.random.normal(base_price, std_dev, periods))
