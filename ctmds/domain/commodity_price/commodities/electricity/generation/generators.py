from ctmds.domain.commodity_price.commodities.electricity.generation.generic import GenericElectricityGenerator


class SolarElectricityGenerator(GenericElectricityGenerator):
    marginal_cost: float = 16.4  # in GBP/MWh
    capacity: float = 9.0  # in GW

class WindElectricityGenerator(GenericElectricityGenerator):
    marginal_cost: float = 19.6  # in GBP/MWh
    capacity: float = 17.0  # in GW

class NuclearElectricityGenerator(GenericElectricityGenerator):
    marginal_cost: float = 65.3  # in GBP/MWh
    capacity: float = 4.2  # in GW

class GasElectricityGenerator(GenericElectricityGenerator):
    marginal_cost: float = 70.2  # in GBP/MWh
    capacity: float = 15.0  # in GW

class PeakElectricityGenerator(GenericElectricityGenerator):
    marginal_cost: float = 101.6  # in GBP/MWh
    capacity: float = 5.0  # in GW

# class CoalElectricityGenerator(GenericElectricityGenerator):
#     capacity: float = 14.5  # in GW
#     marginal_cost: float = 65.3  # in GBP/MWh

# class HydroElectricityGenerator(GenericElectricityGenerator):
#     capacity: float = 14.5  # in GW
#     marginal_cost: float = 65.3  # in GBP/MWh

# class BiomassElectricityGenerator(GenericElectricityGenerator):
#     capacity: float = 14.5  # in GW
#     marginal_cost: float = 65.3  # in GBP/MWh
