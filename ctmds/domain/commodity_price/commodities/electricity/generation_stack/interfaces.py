from datetime import datetime
from typing import Protocol

from ctmds.domain.commodity_price.commodities.electricity.generation_stack.stack import (
    GenerationStack,
)


class IDemandProfileGenerator(Protocol):
    def __call__(
        self,
        periods: int,
        date: datetime,
        base_demand: float,  # GW
        peak_demand: float,  # GW
        seed: int | None = None,
    ) -> list[float]: ...


class IPowerPriceGenerator(Protocol):
    def __call__(
        self,
        periods: int,
        stack: GenerationStack,
        date: datetime,
        demand_profile: IDemandProfileGenerator,
        seed: int | None = None,
    ) -> list[float]: ...
