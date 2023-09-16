from matplotlib import pyplot as plt
import numpy as np
apple = [131.99, 136.18, 123, 131.5, 124.67, 137.02, 145.84, 149.1, 141.71, 149.87, 161.24, 177.51]
micr = [231.79, 233.22, 238.45, 250.1, 247, 271,5, 283,1, 301.5, 282.26, 331.83, 333.49, 336.27]
google =[91.79, 101.1, 103.2, 117.88, 117.85, 122.59, 134.7, 144.83, 133.78, 148, 142.76, 145.05]
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.plot(mes, apple, c = "r") #red
plt.plot(mes, micr, c = "g") #green
plt.plot(mes, google, c = "b") #blue
plt.grid()
plt.show()