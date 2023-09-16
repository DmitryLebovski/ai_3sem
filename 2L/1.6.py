import random
import numpy as np

s = np.random.randint(5, 10)
mtr = np.zeros((s, s))
for i in range(0, s):
    for j in range(0, s):
        n = np.random.randint(0, 30)
        mtr[i][j] = n

print(mtr.shape)
print(mtr.size)
# размерность?????