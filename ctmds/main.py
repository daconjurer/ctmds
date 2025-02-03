from argparse import ArgumentParser

from ctmds.random_generator import generate_random_decimals as generate_random_decimals_iterator
from ctmds.numpy_generator import generate_random_decimals as generate_random_decimals_numpy

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--num", type=int, required=True)
    args = parser.parse_args()

    num: int = args.num

    generate_random_decimals_iterator(num)
    generate_random_decimals_numpy(num)
