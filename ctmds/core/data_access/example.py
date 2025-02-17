from ctmds.domain.commodities.crude.model import CrudeOil

crude_oil = CrudeOil()

print(crude_oil.get_base_price("GB"))
print(crude_oil.get_base_price("DE"))
print(crude_oil.get_base_price("NL"))
print(crude_oil.get_base_price("FR"))
