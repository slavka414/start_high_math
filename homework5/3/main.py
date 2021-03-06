import numpy as np
from matplotlib import pyplot as plt
import math

x = []
y = []
z = []
n = int(input(f'Введите количество попыток:  '))
k = 0
num = int(input(f'Введите желаемое число:  '))
i = 1

while i <= n:
    # input()
    n1 = int(np.random.uniform(0, 36))
    print(n1)
    plt.scatter(i, n1, color = 'green')
    y.append(n1)
    x.append(i)
    i += 1
    if num == n1:
        k += 1

print(f'Количество совпадений: {k}')
c = (math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))
p = c * ((1 / 37) ** k) * ((36 / 37) ** (n - k))
print(f'Вероятность выпадения числа: {p}')
plt.plot(x, y, color = 'red', linewidth = 1)

plt.show()
