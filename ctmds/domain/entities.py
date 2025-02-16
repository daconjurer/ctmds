from __future__ import annotations

import uuid
from datetime import UTC, datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import UUID
from sqlalchemy.types import DECIMAL

from ctmds.core.db.session import Base


class ConcreteBase(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )


# Commodities


class CommodityConfig(ConcreteBase):
    """Base configuration for commodities."""

    __abstract__ = True

    currency: Mapped[str] = mapped_column(String(3))  # ISO 4217
    base_price: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=5, scale=2))
    country_code: Mapped[str] = mapped_column(String(2))  # ISO 3166-1 alpha-2

    def __repr__(self) -> str:
        return (
            f"CommodityConfig(id={self.id}, "
            f"currency={self.currency}, "
            f"base_price={self.base_price}, "
            f"country_code={self.country_code})"
        )


class CrudeOilConfig(CommodityConfig):
    """Configuration for crude oil."""

    __tablename__ = "crude_oil_configs"


class ElectricityConfig(CommodityConfig):
    """Configuration for electricity."""

    __tablename__ = "electricity_configs"


class NaturalGasConfig(CommodityConfig):
    """Configuration for natural gas."""

    __tablename__ = "natural_gas_configs"


# Exchange Rates


class ExchangeRate(ConcreteBase):
    """Exchange rates between currencies."""

    __tablename__ = "exchange_rates"

    from_currency: Mapped[str] = mapped_column(String(3))  # ISO 4217
    to_currency: Mapped[str] = mapped_column(String(3))  # ISO 4217
    rate: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=5, scale=2))
    effective_date: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self) -> str:
        return (
            f"ExchangeRate(id={self.id}, "
            f"from_currency={self.from_currency}, "
            f"to_currency={self.to_currency}, "
            f"rate={self.rate}, "
            f"effective_date={self.effective_date})"
        )
