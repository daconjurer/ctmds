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
from ctmds.domain.constants import CountryCodes

# TODO: Implement persistence for generation stacks
GB_STACK = GenerationStack(
    generators=[
        SolarElectricityGenerator(
            capacity=10.0,
            marginal_cost=15.4,
        ),
        WindElectricityGenerator(
            capacity=10.0,
            marginal_cost=19.6,
        ),
        NuclearElectricityGenerator(
            capacity=10.0,
            marginal_cost=65.3,
        ),
        GasElectricityGenerator(
            capacity=10.0,
            marginal_cost=70.2,
        ),
        PeakElectricityGenerator(
            capacity=10.0,
            marginal_cost=101.6,
        ),
    ]
)


class StackMap:
    """Map of country codes to generation stacks."""

    _STACKS = {
        CountryCodes.GB: GB_STACK,
    }

    @staticmethod
    def get_stack(country_code: CountryCodes) -> GenerationStack:
        """Get the generation stack for a country code."""
        return StackMap._STACKS[country_code]
