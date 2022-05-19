"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def number_guess(r_number, attempt=10):
    guess = int(input(f'Попытайтесь угадать число! У вас осталось {attempt} попыток!\n'))

    if attempt > 0 and guess != r_number:
        print(f'Вы не угадали! Загаданное число {"больше" if r_number > guess else "меньше"} введенного вами!')
        return number_guess(r_number, attempt - 1)
    elif attempt > 0 and guess == r_number:
        print(f'Вы угадали, загаданное число: {r_number}!')
    else:
        print(f'Вы не смогли угадать число за 10 попыток!')


number_guess(random.randint(0, 100))
