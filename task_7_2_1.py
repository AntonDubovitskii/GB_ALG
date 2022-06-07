"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def gnome_sort(sortable_list):
    i = 1
    size = len(sortable_list)
    while i < size:
        if sortable_list[i - 1] <= sortable_list[i]:
            i += 1
        else:
            sortable_list[i - 1], sortable_list[i] = sortable_list[i], sortable_list[i - 1]
            if i > 1:
                i -= 1
    return sortable_list


def get_median(my_list):
    my_list = gnome_sort(my_list)
    return int((len(my_list) - 1) / 2)

#######################################################################################################################


m = 10

rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: \n{get_median(rand_list)}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",               # 0.0010488000116311014
        globals=globals(),
        number=1000))

#######################################################################################################################

m = 100

rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: \n{get_median(rand_list)}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",          # 0.008949199982453138
        globals=globals(),
        number=1000))

#######################################################################################################################

m = 1000

rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: \n{get_median(rand_list)}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",           # 0.09489929996198043
        globals=globals(),
        number=1000))

