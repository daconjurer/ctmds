from datetime import datetime

from ctmds.core.data_access.reader import GenericReader
from ctmds.domain.commodity_price.commodities.electricity.generation_stack.generators import (
    GasElectricityGenerator,
    NuclearElectricityGenerator,
    PeakElectricityGenerator,
    SolarElectricityGenerator,
    WindElectricityGenerator,
)
from ctmds.domain.commodity_price.commodities.electricity.generation_stack.stack import (
    GenerationStack,
)
from ctmds.domain.commodity_price.commodities.electricity.price_generators.basic_stack_price_generator import (
    stack_generation_based_price_generator,
)
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.commodity_price.models.price_generator.generic import (
    GenericDailyPricesGenerator,
)
from ctmds.domain.entities import ElectricityConfig


class ElectricityConfigReader(GenericReader[ElectricityConfig]):
    """Reader for ElectricityConfig."""

    model = ElectricityConfig


class Electricity(GenericCommodity):
    """Implementation of ICommodity for electricity."""

    reader = ElectricityConfigReader()


class ElectricityPriceGenerator:
    """Daily prices generator for electricity."""

    def __call__(self) -> GenericDailyPricesGenerator:
        stack = GenerationStack(
            generators=[
                SolarElectricityGenerator(),
                WindElectricityGenerator(),
                NuclearElectricityGenerator(),
                GasElectricityGenerator(),
                PeakElectricityGenerator(),
            ]
        )

        def power_price_generator(
            periods: int,
            date: datetime,
        ) -> list[float]:
            return stack_generation_based_price_generator(
                periods=periods,
                stack=stack,
                date=date,
            )

        return GenericDailyPricesGenerator(
            prices_generator=power_price_generator,
        )
