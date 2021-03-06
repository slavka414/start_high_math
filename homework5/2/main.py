import  numpy as np
from matplotlib import pyplot as plt

x = []
y = []
z = []
xx = 0

for i in range(0,10):
    # input()
    number = int(np.random.uniform(0, 36))
    print(number)
    # plt.scatter(i, number, color = 'yellow')
    y.append(number)
    x.append(i)
    xx += (number)
    z.append(xx)

plt.plot(x, y, color = 'red', linewidth = 1)
plt.bar(x, z)
plt.show()
