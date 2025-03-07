from pydantic import BaseModel

class GenericElectricityGenerator(BaseModel):
    marginal_cost: float  # in GBP/MWh
    capacity: float  # in GW
