from typing import Sequence

from ctmds.domain.commodity_price.commodities.electricity.generation_stack.generators import (
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

        # TODO: Adjust the price according to the input/current/forecasted demand

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
