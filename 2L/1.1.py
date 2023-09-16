import numpy as np

mtr = np.zeros((8,8))
mtr[1::2,::2] = 1
mtr[::2,1::2] = 1
print(mtr)