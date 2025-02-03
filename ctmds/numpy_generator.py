import numpy as np
import datetime

def generate_random_decimals(num: int) -> np.ndarray:
    start = datetime.datetime.now()
    nums = np.random.randint(0, 9999, size=(num,1)) / 100
    end = datetime.datetime.now()
    print(f"With numpy: {end - start}")
    return nums
