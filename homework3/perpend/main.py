
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 21)
# scatter1 = plt.scatter(0.0, 1.0)
# fig = plt.figure()
y = 2*x
y2 = (-1/2)*x
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
