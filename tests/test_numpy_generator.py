import numpy as np

from ctmds.random_generators.numpy_generator import generate_random_decimals_numpy


def test_generate_random_decimals_numpy():
    # Setup
    num = 10

    # Test
    result = generate_random_decimals_numpy(num)

    # Validation
    assert len(result) == num
    assert all(isinstance(x, np.ndarray) for x in result)
    assert all(0 <= x < 100 for x in result)
