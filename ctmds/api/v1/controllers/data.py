from typing import Annotated, cast

from fastapi import APIRouter, Body, Depends, HTTPException

from ctmds.core.utils.filter_sort import SortParams
from ctmds.domain import exceptions
from ctmds.domain.commodity_price.daily_data import (
    generate_daily_data as commodity_daily_data,
)
from ctmds.domain.commodity_price.models.price import PriceCollection
from ctmds.domain.commodity_price.schemas import DailyDataRequest
from ctmds.domain.exchange_rate.reader import ExchangeRateFilterParams
from ctmds.domain.exchange_rate.schemas import ExchangeRatePublic
from ctmds.domain.exchange_rate.service import ExchangeRateService

router = APIRouter(tags=["data"])


@router.get("/exchange-rate")
async def get_exchange_rate(
    filter: Annotated[ExchangeRateFilterParams, Depends()],
) -> ExchangeRatePublic:
    result = ExchangeRateService().get_current_exchange_rate(
        filter=filter,
        sort=SortParams(sort_by="effective_date", sort_order="desc"),
    )

    if not result:
        raise HTTPException(status_code=404, detail="Exchange rate not found")

    rate = cast(float, result.rate)
    return ExchangeRatePublic(
        from_currency=result.from_currency,
                to_currency=result.to_currency,
            rate=rate,
            effective_date=result.effective_date,
    )


@router.post("/daily-data")
async def generate_daily_data(
    body: Annotated[DailyDataRequest, Body()],
) -> PriceCollection:
    try:
        prices = commodity_daily_data(
            for_date=body.for_date,
            country_code=body.country_code,
            commodity=body.commodity,
            granularity=body.granularity,
            seed=body.seed,
        )
    except exceptions.CoreException as e:
        raise HTTPException(status_code=400, detail=str(e))

    return prices
