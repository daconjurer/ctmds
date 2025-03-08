from datetime import datetime

from ctmds.domain.commodity_price.commodities.natural_gas.model import NaturalGas
from ctmds.domain.commodity_price.commodities.natural_gas.price_generators.basic import (
    gas_price_generator,
)
from ctmds.domain.commodity_price.models.commodity.generic import GenericCommodity
from ctmds.domain.commodity_price.models.price_generator.generic import (
    GenericDailyPricesGenerator,
    ICreateDailyPricesGenerator,
)
from ctmds.domain.constants import CountryCodes
from ctmds.domain.data_generators.daily_timestamps import (
    get_day_periods,
    get_last_period,
)


class GasPriceGenerator(ICreateDailyPricesGenerator):
    """Daily prices generator for electricity."""

    commodity: GenericCommodity = NaturalGas()

    def __init__(self, country_code: CountryCodes):
        self.country_code = country_code

    def __call__(self) -> GenericDailyPricesGenerator:
        def natural_gas_price_generator(
            date: datetime,
        ) -> list[float]:
            periods = get_day_periods(date, self.country_code)
            last_period = get_last_period(date, self.country_code)

            base_price = self.commodity.get_price(
                country_code=self.country_code,
                period=last_period,
            )
            return gas_price_generator(
                date=date,
                periods=periods,
                base_price=base_price,
            )

        return GenericDailyPricesGenerator(
            prices_generator=natural_gas_price_generator,
        )
