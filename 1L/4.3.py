from math import*
from matplotlib import pyplot as plt
import numpy as np
from numpy import trapz

x = np.arange(0.0, 10, 1)
y = np.abs(np.fabs(np.cos(x*np.exp(np.cos(x)+np.log(x+1)))))
plt.grid()
plt.plot(x, y, c = "r")
plt.fill_between(x, y)

plt.show()
area = trapz(y)
print (area)
