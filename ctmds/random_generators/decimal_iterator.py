from typing import Iterator
from decimal import Decimal
import random

def random_decimal() -> Iterator[Decimal]:
    yield Decimal(random.randrange(0, 9999))/100

def generate_random_decimals_iterator(num: int) -> list[Decimal]:
    return [next(random_decimal()) for _ in range(num)]
