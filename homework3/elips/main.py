
import numpy as np
import matplotlib.pyplot as plt

rx = int(input('Введите радиус по х:  '))
ry = int(input('Введите радиус по y:  '))
x0 = int(input('Введите сдвиг по 0х:  '))
y0 = int(input('Введите сдвиг по 0y:  '))

t = np.linspace(0, 2*np.pi, 500)
scatter1 = plt.scatter(x0, y0)
plt.plot(x0+rx*np.cos(t), y0+ry*np.sin(t))
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
