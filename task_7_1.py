"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit


def reversed_bubble_sort(my_list):
    n = 1

    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1

    return my_list


def reversed_bubble_sort_flag(my_list):
    n = 1

    while n < len(my_list):
        flag = False
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                flag = True
        n += 1
        if n > 1 and not flag:
            return my_list

    return my_list


rand_list = [randint(-100, 100) for _ in range(10)]

print(f'Исходный массив: {rand_list}')
print(f'Отсортированный массив, функция reversed_bubble_sort(): {reversed_bubble_sort(rand_list[:])}')
print(f'Отсортированный массив, функция reversed_bubble_sort_flag(): {reversed_bubble_sort_flag(rand_list[:])}\n')


print(f"Время сортировки случайного массива: \n")
print(
    timeit(
        "reversed_bubble_sort(rand_list[:])",          # 0.3181339000002481
        globals=globals(),
        number=100000))

print(
    timeit(
        "reversed_bubble_sort_flag(rand_list[:])",     # 0.24966270005097613
        globals=globals(),
        number=100000))

#######################################################################################################################
"""
Наилучший вариант для модернизированной сортировки пузырьком
"""
sorted_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(f"\nНаилучший вариант, фиксированный массив: \n")
print(
    timeit(
        "reversed_bubble_sort(sorted_list[:])",         # 0.2821267999825068
        globals=globals(),
        number=100000))

print(
    timeit(
        "reversed_bubble_sort_flag(sorted_list[:])",    # 0.049810900003649294
        globals=globals(),
        number=100000))

#######################################################################################################################
"""
Наихудший вариант для модернизированной сортировки пузырьком
"""
sorted_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"\nНаихудший вариант, фиксированный массив: \n")
print(
    timeit(
        "reversed_bubble_sort(sorted_list2[:])",         # 0.49471439997432753
        globals=globals(),
        number=100000))

print(
    timeit(
        "reversed_bubble_sort_flag(sorted_list2[:])",    # 0.5232516000396572
        globals=globals(),
        number=100000))

#######################################################################################################################
"""
Частично отсортированный массив
"""
half_sorted_list3 = [60, 8, 7, 10, 55, 11, 6, 5, 4, 3, 2, 1, 0]

print(f"\nНаполовину отсортированный массив: ")
print(
    timeit(
        "reversed_bubble_sort(half_sorted_list3[:])",         # 4.0749884999822825
        globals=globals(),
        number=1000000))

print(
    timeit(
        "reversed_bubble_sort_flag(half_sorted_list3[:])",    # 2.1888450999977067
        globals=globals(),
        number=1000000))
"""
Вывод:

Были написаны функции reversed_bubble_sort() и reversed_bubble_sort_flag(), сортирующие переданные им массивы методом
"пызырька" в обратном порядке. Во второй из них применено дополнение к алгоритму - если после очередного прохода по 
массиву не было произведено ни одной перестановки, функция завершает работу и возвращает массив - так как он уже 
отсортирован, нет смысла совершать последующие проходы.

Были проведены замеры времени выполнения данных функций. При сортировке массива состоящего из случайных элементов,
разница во времени выполнения также была случайной, в зависимости от сгенерированных массивов. 
Функция reversed_bubble_sort_flag() работает быстрее в том случае, если весь массив или оставшаяся его часть уже 
расположены в требуемом порядке. Разница в скорости возникает из-за того, что в обычной реализации сортировки 
"пузырьком" нет никакого контроля за состоянием массива, в любом случае будет совершено фиксированное количество 
проходов, даже если массив изначально отсортирован, что дает алгоритмическую сложность O(N^2). 
Добавление проверки позволяет прекратить работу функции после первого прохода, в данном случае сложность окажется O(N).

В наихудшем варианте (массив осортирован в обратном к требуемому порядке), количество проходов 
у обеих функций одинаковое и соответственно скорость выполнения практически одинакова. При наилучшем варианте (массив 
уже отсортирован в заданном порядке) функция с проверкой работала в 5,7 раз быстрее. При использовании наполовину 
отсортированного массива, функция с проверкой сработала в два раза быстрее.

Таким образом использование проверки действительно ускоряет работу сортировки "пузырьком", в некоторых сценариях.
"""

