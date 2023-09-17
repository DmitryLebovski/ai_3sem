from matplotlib import pyplot as plt
import numpy as np
apple = [131.99, 136.18, 123, 131.5, 124.67, 137.02, 145.84, 149.1, 141.71, 149.87, 161.24, 177.51]
micr = [222.53, 235.06, 235.90, 238.47, 254.40, 251.21, 269.51, 286.36, 302.87, 282.12, 331.36, 335.15, 310.41]
google =[91.79, 101.1, 103.2, 117.88, 117.85, 122.59, 134.7, 144.83, 133.78, 148, 142.76, 145.05]
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.plot(apple, label='Apple', c = "r") #red
plt.plot(micr, label='Microsoft', c = "g") #green
plt.plot(google, label='Google', c = "b") #blue
plt.legend()
plt.grid()
plt.show()