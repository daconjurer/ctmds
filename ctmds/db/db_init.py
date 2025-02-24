from datetime import UTC, datetime

from ctmds.core.db.session import get_session, init_db, teardown_db
from ctmds.domain.entities import (
    CrudeOilConfig,
    ElectricityConfig,
    ExchangeRate,
    NaturalGasConfig,
)

# Initialize database
teardown_db()
init_db()

# Add commodities configs
with next(get_session()) as db:
    config_gb = CrudeOilConfig(currency="GBP", base_price=57.37, country_code="GB")
    config_de = CrudeOilConfig(currency="EUR", base_price=69.03, country_code="DE")
    config_nl = CrudeOilConfig(currency="EUR", base_price=69.03, country_code="NL")
    config_fr = CrudeOilConfig(currency="EUR", base_price=69.03, country_code="FR")

    db.add_all([config_gb, config_de, config_nl, config_fr])
    db.flush()

    config_gb = ElectricityConfig(currency="GBP", base_price=108.50, country_code="GB")
    config_de = ElectricityConfig(currency="EUR", base_price=130.58, country_code="DE")
    config_nl = ElectricityConfig(currency="EUR", base_price=130.58, country_code="NL")
    config_fr = ElectricityConfig(currency="EUR", base_price=130.58, country_code="FR")

    db.add_all([config_gb, config_de, config_nl, config_fr])
    db.flush()

    config_gb = NaturalGasConfig(currency="GBP", base_price=2.67, country_code="GB")
    config_de = NaturalGasConfig(currency="EUR", base_price=3.21, country_code="DE")
    config_nl = NaturalGasConfig(currency="EUR", base_price=3.21, country_code="NL")
    config_fr = NaturalGasConfig(currency="EUR", base_price=3.21, country_code="FR")

    db.add_all([config_gb, config_de, config_nl, config_fr])
    db.commit()

# Add exchange rates
with next(get_session()) as db:
    rate_gbp_eur = ExchangeRate(
        from_currency="GBP",
        to_currency="EUR",
        rate=1.19,
        effective_date=datetime.now(UTC),
    )

    db.add(rate_gbp_eur)
    db.commit()
