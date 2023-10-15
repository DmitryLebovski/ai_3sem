import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from numpy.random import *

delta = 1.0
x = linspace(-5,5,11)
y = x**2 + delta * (rand(11) - 0.5)
x += delta * (rand(11) - 0.5)

x.tofile('x_data.txt', '\n')
y.tofile('y_data.txt', '\n')

x = fromfile('x_data.txt', float, sep='\n')
y = fromfile('y_data.txt', float, sep='\n')


m1 = vstack((x, ones(11))).T
m2 = vstack((x**2, x, ones(11))).T
m3 = vstack((x**3, x**2, x, ones(11))).T
s1 = np.linalg.lstsq(m1, y, rcond = None)[0]
s2 = np.linalg.lstsq(m2, y, rcond = None)[0]
s3 = np.linalg.lstsq(m3, y, rcond = None)[0]

x_prec = linspace(-5, 5, 101)

plt.plot(x,y,'D')

plt.plot(x_prec, s2[0]*x_prec + s2[1], '-', lw = 1)
plt.grid()
plt.plot(x_prec, s2[0] * x_prec**2 + s2[1]*x_prec + s2[2], '-', lw = 1)
plt.grid()
plt.plot(x_prec, s3[0] * x_prec**3 + s3[1] * x_prec**2 + s3[2]*x_prec + s3[3], '-', lw = 2)
plt.grid()
plt.savefig("параболы.png")