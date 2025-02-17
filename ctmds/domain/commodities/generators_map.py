from ctmds.domain.commodities.crude.price_generator import oil_price_generator
from ctmds.domain.commodities.electricity.price_generator import power_price_generator
from ctmds.domain.commodities.natural_gas.price_generator import gas_price_generator
from ctmds.domain.constants import SupportedCommodities
from ctmds.domain.models.price_generator.generic import GenericDailyPricesGenerator


class GeneratorMap:
    """Map of supported commodities to their implementations."""

    _generators_map = {
        SupportedCommodities.CRUDE: oil_price_generator,
        SupportedCommodities.NATURAL_GAS: gas_price_generator,
        SupportedCommodities.POWER: power_price_generator,
    }

    @staticmethod
    def get_generator(commodity: SupportedCommodities) -> GenericDailyPricesGenerator:
        """Get the commodity implementation for a given commodity."""
        generator = GeneratorMap._generators_map.get(commodity, oil_price_generator)
        return GenericDailyPricesGenerator(prices_generator=generator)
