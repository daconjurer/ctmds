import random
from decimal import Decimal
from typing import Iterator


def random_decimal() -> Iterator[Decimal]:
    yield Decimal(random.randrange(0, 9999)) / 100


def generate_random_decimals_iterator(num: int) -> list[Decimal]:
    return [next(random_decimal()) for _ in range(num)]
