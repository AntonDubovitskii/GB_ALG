"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def get_median(my_list):
    """
    Поиск медианы через удаление максимальных элементов массива
    """
    support_list = my_list
    for i in range(len(support_list) // 2):
        my_list.remove(max(support_list))
    return max(support_list)

#######################################################################################################################


m = 10
rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: {get_median(rand_list[:])}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",      # 0.002084899984765798
        globals=globals(),
        number=1000))

#######################################################################################################################

m = 100
rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: {get_median(rand_list[:])}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",         # 0.12805449997540563
        globals=globals(),
        number=1000))

#######################################################################################################################

m = 1000
rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: {get_median(rand_list[:])}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",         # 14.332492000015918
        globals=globals(),
        number=1000))

