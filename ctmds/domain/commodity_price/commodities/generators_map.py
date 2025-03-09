from ctmds.domain.commodity_price.commodities.crude.price_generator import (
    CrudePriceGenerator,
)
from ctmds.domain.commodity_price.commodities.electricity.price_generator import (
    ElectricityPriceGenerator,
)
from ctmds.domain.commodity_price.commodities.natural_gas.price_generator import (
    GasPriceGenerator,
)
from ctmds.domain.commodity_price.models.price_generator.generic import (
    ICreateDailyPricesGenerator,
)
from ctmds.domain.constants import CountryCodes, SupportedCommodities


class GeneratorMap:
    """Map of supported commodities to their implementations."""

    _generators_map = {
        SupportedCommodities.CRUDE: CrudePriceGenerator,
        SupportedCommodities.NATURAL_GAS: GasPriceGenerator,
        SupportedCommodities.POWER: ElectricityPriceGenerator,
    }

    @staticmethod
    def get_generator(
        commodity: SupportedCommodities,
        country_code: CountryCodes,
    ) -> ICreateDailyPricesGenerator:
        """Get the commodity implementation for a given commodity."""
        generator = GeneratorMap._generators_map.get(
            commodity,
            ElectricityPriceGenerator,
        )
        return generator(country_code)
