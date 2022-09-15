'''Игра компьютер угадает число меньше чем за 20 попыток'''
import numpy as np


def game(number):
    """Рандомно угадываем число

    Args:
        number (int): Загаданное число.

    Returns:
        int: Число попыток
    """
    min = 1
    max = 101

    count = 0

    while True:
        count += 1
        mid = int((min + max) / 2)

        if mid > number:  # если среднее больше загаданного, то опускаем верхнюю границу
            max = mid

        elif mid < number:  # если наоборот, то поднимаем нижхнюю границу
            min = mid

        else:
            return count
            break  # конец игры выход из цикла


def score_game(game) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    # загадали списоконлайн переводчик чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток(ки)")


score_game(game)
