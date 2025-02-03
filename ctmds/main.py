from datetime import datetime
from argparse import ArgumentParser

from ctmds.random_generators.decimal_iterator import generate_random_decimals_iterator
from ctmds.random_generators.numpy_generator import generate_random_decimals_numpy

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--num", type=int, required=True)
    args = parser.parse_args()

    num: int = args.num

    start = datetime.now()
    generate_random_decimals_iterator(num)
    end = datetime.now()
    print(f"With iterator: {end - start}")

    start = datetime.now()
    generate_random_decimals_numpy(num)
    end = datetime.now()
    print(f"With numpy: {end - start}")
