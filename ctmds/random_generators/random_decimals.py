from datetime import datetime

from ctmds.random_generators.decimal_iterator import generate_random_decimals_iterator
from ctmds.random_generators.numpy_generator import generate_random_decimals_numpy


def generate_random_decimals(num: int):
    start: datetime = datetime.now()
    generate_random_decimals_iterator(num)
    end: datetime = datetime.now()
    print(f"With iterator: {end - start}")

    start: datetime = datetime.now()
    generate_random_decimals_numpy(num)
    end: datetime = datetime.now()
    print(f"With numpy: {end - start}")
