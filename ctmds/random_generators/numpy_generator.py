import numpy as np

def generate_random_decimals_numpy(num: int) -> np.ndarray:
    nums = np.random.randint(0, 9999, size=(num,1)) / 100
    return nums
