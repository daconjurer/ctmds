from ctmds.domain.commodity_price.commodities.electricity.generation_stack.generators import (
    CoalElectricityGenerator,
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
        WindElectricityGenerator(
            capacity=19.7,
            marginal_cost=19.6,
        ),
        GasElectricityGenerator(
            capacity=16.6,
            marginal_cost=70.2,
        ),
        NuclearElectricityGenerator(
            capacity=10.0,
            marginal_cost=40.3,
        ),
        SolarElectricityGenerator(
            capacity=9.0,
            marginal_cost=15.4,
        ),
        PeakElectricityGenerator(
            capacity=10.0,
            marginal_cost=101.6,
        ),
    ]
)

FR_STACK = GenerationStack(
    generators=[
        NuclearElectricityGenerator(
            capacity=18.7,
            marginal_cost=42.9,
        ),
        WindElectricityGenerator(
            capacity=11.5,
            marginal_cost=19.3,
        ),
        GasElectricityGenerator(
            capacity=12.0,
            marginal_cost=67.9,
        ),
        PeakElectricityGenerator(
            capacity=11.4,
            marginal_cost=100.0,
        ),
    ]
)

DE_STACK = GenerationStack(
    generators=[
        WindElectricityGenerator(
            capacity=12.2,
            marginal_cost=18.5,
        ),
        GasElectricityGenerator(
            capacity=18.0,
            marginal_cost=68.6,
        ),
        SolarElectricityGenerator(
            capacity=10.0,
            marginal_cost=14.9,
        ),
        CoalElectricityGenerator(
            capacity=19.4,
            marginal_cost=80.4,
        ),
        PeakElectricityGenerator(
            capacity=12.0,
            marginal_cost=99.8,
        ),
    ]
)

NL_STACK = GenerationStack(
    generators=[
        GasElectricityGenerator(
            capacity=16.9,
            marginal_cost=66.0,
        ),
        WindElectricityGenerator(
            capacity=7.4,
            marginal_cost=17.1,
        ),
        SolarElectricityGenerator(
            capacity=6.0,
            marginal_cost=13.4,
        ),
        PeakElectricityGenerator(
            capacity=9.8,
            marginal_cost=99.2,
        ),
    ]
)


class StackMap:
    """Map of country codes to generation stacks."""

    _STACKS = {
        CountryCodes.GB: GB_STACK,
        CountryCodes.FR: FR_STACK,
        CountryCodes.DE: DE_STACK,
        CountryCodes.NL: NL_STACK,
    }

    @staticmethod
    def get_stack(country_code: CountryCodes) -> GenerationStack:
        """Get the generation stack for a country code."""
        return StackMap._STACKS.get(country_code, GB_STACK)
