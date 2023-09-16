import random
from math import*
from matplotlib import pyplot as plt
import random

fx = []
for i in range(1, 11):
    x = random.random()
    fx.append(round(((sqrt(1 + e**(sqrt(x)) + cos(x**2)))/(abs(1 - (sin(x)**3)))) + log10(abs(2*x)), 3))
fx2 = []
for i in range(len(fx) // 2):
    fx2.append(fx[i])

plt.scatter(list(range(0, 5)), fx2)
plt.show()
plt.plot(list(range(0, 10)), fx)
plt.show()

print(fx)
print(fx2)