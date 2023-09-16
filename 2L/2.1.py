import numpy as np
import pandas as pd
a = np.array((5, 0, 5))
b = np.array((3, 3, 3))
sq = np.square(a - b)
sum_sq = np.sum(sq)
dist = np.sqrt(sum_sq)
print(dist)