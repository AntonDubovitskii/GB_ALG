"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from cProfile import run
from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1, 2, 12, 5234, 3, 5, 6, 1, 3, 4, 4, 90, 3]

"""
Далее функции используются массив напрямую, не через аргумент. Насколько я знаю это нарушение, но буду придерживаться
заданного стиля.
"""


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    # Вариант из будущего урока :) Но было бы странно не применить
    result = Counter(array).most_common(1)
    return f'Чаще всего встречается число {result[0][0]}, ' \
           f'оно появилось в массиве {result[0][1]} раз(а)'


def func_4():
    # Изящный вариант, но к сожалению уже засветился как стандартное решение. Оставил для профилирования
    result = max(array, key=array.count)
    return f"Чаще всего встречается число {result}, оно появилось в массиве" \
           f" {array.count(result)} раз(а)"


def func_5():
    # Вариант через словарь
    mydict = {}
    for i in array:
        dict_key = i
        if dict_key not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    result_key = max(mydict, key=mydict.get)
    return f"Чаще всего встречается число {result_key}, оно появилось в массиве" \
           f" {mydict[result_key]} раз(а)"


print(func_1())
print(timeit('func_1()', globals=globals()))        # 2.1126327000001766

print(func_2())
print(timeit('func_2()', globals=globals()))        # 2.4570126000007804

print(func_3())
print(timeit('func_3()', globals=globals()))        # 1.9125499000001582

print(func_4())
print(timeit('func_4()', globals=globals()))        # 2.006737499999872

print(func_5())
print(timeit('func_5()', globals=globals()))        # 1.363749999999527

"""
Вывод:

Предложено три дополнительных алгоритма. Для всех пяти алгоритмов проведены замеры времени выполнения при помощи
timeit. Изначальные два алгоритма оказались наименее эффективными. Лучший результат показал алгоритм, использующий
возможности словаря - он оказался в 1,7 раз быстрее самого медленного алгоритма, использующего списки.
"""

