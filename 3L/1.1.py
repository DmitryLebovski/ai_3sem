import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

d1 = np.array([5, 3, 1])
d2 = np.array([1, 7, 9])
d3 = np.array([5, 7, 10])
d4 = np.array([4, 0, 1])


print('d1 - d2:')
print(np.linalg.norm(d1 - d2))
print(np.linalg.norm(d1 - d2) ** 2)
print(np.linalg.norm(d1 - d2, ord=np.inf))
print(np.linalg.norm(d1 - d2, ord=1))
print('\n')

print('d1 - d3:')
print(np.linalg.norm(d1 - d3))
print(np.linalg.norm(d1 - d3) ** 2)
print(np.linalg.norm(d1 - d3, ord=np.inf))
print(np.linalg.norm(d1 - d3, ord=1))
print('\n')

print('d1 - d4:')
print(np.linalg.norm(d1 - d4))
print(np.linalg.norm(d1 - d4) ** 2)
print(np.linalg.norm(d1 - d4, ord=np.inf))
print(np.linalg.norm(d1 - d4, ord=1))
print('\n')

print('d2 - d3:')
print(np.linalg.norm(d2 - d3))
print(np.linalg.norm(d2 - d3) ** 2)
print(np.linalg.norm(d2 - d3, ord=np.inf))
print(np.linalg.norm(d2 - d3, ord=1))
print('\n')

print('d2 - d4:')
print(np.linalg.norm(d2 - d4))
print(np.linalg.norm(d2 - d4) ** 2)
print(np.linalg.norm(d2 - d4, ord=np.inf))
print(np.linalg.norm(d2 - d4, ord=1))
print('\n')

print('d3 - d4:')
print(np.linalg.norm(d3 - d4))
print(np.linalg.norm(d3 - d4) ** 2)
print(np.linalg.norm(d3 - d4, ord=np.inf))
print(np.linalg.norm(d3 - d4, ord=1))
print('\n')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(d1[0], d1[1], d1[2])
ax.scatter(d2[0], d2[1], d2[2])
ax.scatter(d3[0], d3[1], d3[2])
ax.scatter(d4[0], d4[1], d4[2])
plt.show()