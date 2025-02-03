import datetime
from typing import Iterator
from decimal import Decimal
import random

def random_decimal() -> Iterator[Decimal]:
    yield Decimal(random.randrange(0, 9999))/100

def generate_random_decimals(num: int) -> None:
    start = datetime.datetime.now()

    for _ in range(num):
        next(random_decimal())

    end = datetime.datetime.now()
    print(f"With random: {end - start}")
