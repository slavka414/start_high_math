import numpy as np
from matplotlib import pyplot as plt

i = 1
k = 1
a = 3
b = 5

x = np.linspace(-10, 10, 100)
while i < 5 :
    i += 1
    y = plt.plot(k * np.cos(x - a) + b)
    k += 1
    a += 2
    b += 3

plt.show()