"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

common_dict = {}
ord_dict = OrderedDict()

#####################################################################################


def add_common(my_dict):
    for i in range(1000):
        common_dict[i] = i


def add_ordered(my_dict):
    for i in range(1000):
        ord_dict[i] = i


print('\nРезультаты замера времени добавления элементов: ')
print(timeit("add_common(common_dict)", globals=globals(), number=100000))   # 2.303960500001267
print(timeit("add_ordered(ord_dict)", globals=globals(), number=100000))     # 3.14265019999948
####################################################################################


def delete_common(my_dict):
    for i in range(len(my_dict)):
        del my_dict[i]


def delete_ordered(my_dict):
    for i in range(len(my_dict)):
        del my_dict[i]


add_ordered(1000000)
add_common(1000000)

print('\nРезультаты замера времени удаления элементов: ')
print(timeit("delete_common(common_dict)", globals=globals(), number=10000000))  # 0.7907494000028237
print(timeit("delete_ordered(ord_dict)", globals=globals(), number=10000000))    # 0.8092293000008794
####################################################################################


def update_common(len):
    for i in range(len):
        common_dict[i] = i + 10


def update_ordered(len):
    for i in range(len):
        ord_dict[i] = i + 10


add_ordered(1000000)
add_common(1000000)

print('\nРезультаты замера времени обновления элементов: ')
print(timeit("update_common(1000000)", globals=globals(), number=10))    # 0.38126849999753176
print(timeit("update_ordered(1000000)", globals=globals(), number=10))   # 0.49907119999988936

"""
Вывод:

Были проведены замеры скорости выполнения базовых операций обычного словаря Python и OrderedDict из модуля collections.
Результаты показывают, что OrderedDict медленнее обычной реализации словаря при добавлении и обновлении элементов, 
скорость удаления элементов по ключу практически одинаковая. Это связано с тем, что OrderedDict создавался с целью
добавления нового функционала, скорость и занимаемая память были вторичны. С выходом Python 3.6 стандартные словари
также стали упорядоченными, следовательно при необходимости получить от программы максимальную скорость, следует
использовать их. Если скорость не критична, для удобства можно использовать OrderedDict, так как он предоставляет
дополнительные возможности, сокращающие количество кода и соответственно ускоряющие разработку, например метод
.popitem() и .move_to_end(), а также возможность проверки словарей на эквивалентность.
"""

