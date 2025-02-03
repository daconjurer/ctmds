from decimal import Decimal

from ctmds.random_generators.decimal_iterator import generate_random_decimals_iterator


def test_generate_random_decimals_iterator():
    # Setup
    num = 10

    # Test
    result = generate_random_decimals_iterator(num)

    # Validation
    assert len(result) == num
    assert all(isinstance(x, Decimal) for x in result)
    assert all(0 <= x < 100 for x in result)
