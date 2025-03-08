from datetime import datetime

from ctmds.domain.commodity_price.commodities.electricity.price_generators.basic_stack_based import (
    stack_generation_based_price_generator,
)
from ctmds.domain.commodity_price.models.price_generator.generic import (
    GenericDailyPricesGenerator,
)
from ctmds.domain.constants import CountryCodes


class ElectricityPriceGenerator:
    """Daily prices generator for electricity."""

    def __init__(self, country_code: CountryCodes):
        self.country_code = country_code

    def __call__(self) -> GenericDailyPricesGenerator:
        def power_price_generator(
            date: datetime,
        ) -> list[float]:
            return stack_generation_based_price_generator(
                country_code=self.country_code,
                date=date,
            )

        return GenericDailyPricesGenerator(
            prices_generator=power_price_generator,
        )
