'''Игра компьютер угадает число меньше чем за 20 попыток'''
import numpy as np

min = 1
max = 101


number = np.random.randint(min, max)
np.random.seed(42)
count = 0

while True:
    count += 1
    mid = int((min + max) / 2)

    if mid > number: # если среднее больше загаданного, то опускаем верхнюю границу
        max = mid

    elif mid < number: # если наоборот, то поднимаем нижхнюю границу
        min = mid

    else:
        print(f"Компьютер угадал число за {count} попыток. Это число {number}")
        break  # конец игры выход из цикла
        