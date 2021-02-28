import numpy as np
import matplotlib.pyplot as plt

r = int(input('Введите радиус:  '))
x0 = int(input('Введите координату по 0х центра окружности:  '))
y0 = int(input('Введите координату по 0y центра окружности:  '))

x = np.linspace(-r + x0, r + x0, 1000)
scatter1 = plt.scatter(x0, y0)
y = np.sqrt(r ** 2 - (x - x0) ** 2) + y0
y2 = np.sqrt(r ** 2 - (x - x0) ** 2) * (-1) + y0
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
