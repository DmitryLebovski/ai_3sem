import random
import numpy as np

mtr = np.arange(25).reshape(5,5)
for i in range(0, 5):
    for j in range(0,5):
        mtr[i][j] = random.randint(0, 4)
print(mtr)

mtr = np.zeros((5, 5))
mtr += np.arange(5)
print(mtr)