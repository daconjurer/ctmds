# from ctmds.domain.commodity_price.commodities.crude.price_generator import (
#     oil_price_generator,
# )
from typing import Protocol

from ctmds.domain.commodity_price.commodities.electricity.model import (
    ElectricityPriceGenerator,
)

# from ctmds.domain.commodity_price.commodities.natural_gas.price_generator import (
#     gas_price_generator,
# )
from ctmds.domain.commodity_price.models.price_generator.generic import (
    GenericDailyPricesGenerator,
)
from ctmds.domain.constants import SupportedCommodities


class ICreateDailyPricesGenerator(Protocol):
    """Protocol for creating daily prices generators."""

    def __call__(self) -> GenericDailyPricesGenerator:
        """Create a daily prices generator."""
        ...


class GeneratorMap:
    """Map of supported commodities to their implementations."""

    _generators_map = {
        # SupportedCommodities.CRUDE: oil_price_generator,
        # SupportedCommodities.NATURAL_GAS: gas_price_generator,
        SupportedCommodities.POWER: ElectricityPriceGenerator(),
    }

    @staticmethod
    def get_generator(
        commodity: SupportedCommodities,
    ) -> ICreateDailyPricesGenerator:
        """Get the commodity implementation for a given commodity."""
        generator = GeneratorMap._generators_map.get(
            commodity,
            ElectricityPriceGenerator(),
        )
        return generator
