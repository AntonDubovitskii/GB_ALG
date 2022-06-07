"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit
from statistics import median


def get_median(mylist):
    return median(mylist)

#######################################################################################################################


m = 10

rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(rand_list)
print(f'Значение медианы: {get_median(rand_list)}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",    # 0.000416700029745698
        globals=globals(),
        number=1000))

#######################################################################################################################

m = 100

rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: {get_median(rand_list)}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",         # 0.003596799972001463
        globals=globals(),
        number=1000))

#######################################################################################################################

m = 1000

rand_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'\n{rand_list}')
print(f'Значение медианы: {get_median(rand_list)}')

print('Время выполнения: ')
print(
    timeit(
        "get_median(rand_list[:])",         # 0.10868559998925775
        globals=globals(),
        number=1000))

"""
Вывод по трём вариантам задания 7_2:

Реализованы три способа нахождения медианы в массиве размера 2m + 1 - через сортировку массива, через удаление
максимальных элементов массива в цикле, а также при помощи функции median модуля statistics.

Были проведены замеры времени выполнения для каждого способа. Функции median модуля statistics опережает по скорости
способ с сортировкой при m = 10 и 100, при m = 1000 скорость примерно одинаковая. Это связано с тем, что в 
отсортированном массиве нечетной длины, медиану можно найти при помощи простой арифметической операции и операции
получения элемента по индексу.  

Самым медленным способом оказался поиск медианы без сортировки, так как алгоритм подразумевает удаление элементов из
списка, это приводит к необходимости сдвигать остальные элементы, что дает сильную просадку в скорости на больших 
массивах.

"""
