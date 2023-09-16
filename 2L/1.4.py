import random
import numpy as np

s = int(input())
mtr = np.zeros((s,s))
for i in range(0, s):
    for j in range(0, s):
        if (i == 0 or i == s-1) or (j == 0 or j == s-1):
            mtr[i][j] = 1

print(mtr)