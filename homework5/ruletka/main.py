import  numpy as np


for i in range(0,10):
    input()
    number = int(np.random.uniform(0, 72))
    print(number // 2)
    if number % 2 == 0 and number >> 0:
        print('Чёрный')
    elif number % 2 == 1 and number >> 0:
        print('Красный')
