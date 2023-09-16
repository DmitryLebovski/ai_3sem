import random
import numpy as np

arr = np.array([np.random.randint(0,10) for i in range(10)])
print(np.sort(arr)[::-1])