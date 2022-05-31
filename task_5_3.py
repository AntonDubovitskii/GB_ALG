"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit


class DequeClass:
    def __init__(self, mylist):
        self.mylist = mylist

    def show(self):
        return self.mylist

    def get_element(self, elem):
        return self.mylist[elem]

    def is_empty(self):
        return self.mylist == []

    def add_to_end(self, elem):
        self.mylist.append(elem)

    def add_to_front(self, elem):
        self.mylist.insert(0, elem)

    def remove_from_end(self):
        self.mylist.pop()

    def remove_from_front(self):
        self.mylist.pop(0)

    def extend_to_left(self, extendlist):
        length = len(extendlist)
        for i in range(length):
            self.mylist.insert(0, extendlist[i])
            """
            Специально не стал добавлять в правильном порядке, так как .extendleft из collections.deque также 
            добавляет элементы в обратном порядке.
            """

    def extend(self, extendlist):
        self.mylist.extend(extendlist)

    def size(self):
        return len(self.mylist)


def get_element(just_list, elem):
    """
    Отдельная функция для сравнения
    """
    return just_list[elem]


my_deque = DequeClass([i+10 for i in range(1000000)])
collections_deque = deque([i+10 for i in range(1000000)])
my_extend_list = [i for i in range(1000)]

just_list = [i+10 for i in range(1000)]


#######################################################################################################################


print('\nРезультаты замера времени добавления элементов в начало дека: ')
print(timeit("my_deque.add_to_front('Новый элемент в начало')", globals=globals(), number=10000))  # 2.386527099999512
print(timeit("collections_deque.appendleft('Новый элемент в начало')", globals=globals(), number=10000))  # 0.0002086

######################################################################################################################


print('\nРезультаты замера времени добавления элементов в конец дека: ')
print(timeit("my_deque.add_to_end('Новый элемент в конец')", globals=globals(), number=100000))  # 0.006827299999713432
print(timeit("collections_deque.append('Новый элемент в конец')", globals=globals(), number=100000))  # 0.00229519999993

#######################################################################################################################


print('\nРезультаты замера времени удаления элементов из начала дека: ')
print(timeit("my_deque.remove_from_front()", globals=globals(), number=10000))  # 5.75300309999875
print(timeit("collections_deque.popleft()", globals=globals(), number=10000))   # 0.0002583999994385522

#######################################################################################################################


print('\nРезультаты замера времени удаления элементов из конца дека: ')
print(timeit("my_deque.remove_from_end()", globals=globals(), number=1000000))  # 0.06137440000020433
print(timeit("collections_deque.pop()", globals=globals(), number=1000000))     # 0.02304750000257627

#######################################################################################################################


print('\nРезультаты замера времени присоединения списка к концу дека: ')
print(timeit("my_deque.extend(my_extend_list)", globals=globals(), number=10000))           # 0.11616499999945518
print(timeit("collections_deque.extend(my_extend_list)", globals=globals(), number=10000))  # 0.04741510000167182

#######################################################################################################################


print('\nРезультаты замера времени присоединения списка к началу дека: ')
print(timeit("my_deque.extend_to_left(my_extend_list)", globals=globals(), number=1))       # 5.304381999998441
print(timeit("collections_deque.extendleft(my_extend_list)", globals=globals(), number=1))  # 8.000002708286047e-06

#######################################################################################################################


print('\nПолучение элемента, 1 вызов: ')
print(timeit("get_element(just_list, 100)", globals=globals(), number=1))  # отдельная функция 8.00002453615889e-07
print(timeit("my_deque.get_element(100)", globals=globals(), number=1))  # метод объекта 1.0999974620062858e-06
print(timeit("just_list[100]", globals=globals(), number=1))         # взятие элемента списка 1.00000761449337e-07
print(timeit("collections_deque[100]", globals=globals(), number=1))  # взятие элемента deque 5.599998985417187e-06

#######################################################################################################################


print('\nПолучение элемента, 1000000 вызовов: ')
print(timeit("get_element(just_list, 100)", globals=globals(), number=1000000))  # отдельная функция 0.04160190000038710
print(timeit("my_deque.get_element(100)", globals=globals(), number=1000000))  # метод объекта 0.04849110000213841
print(timeit("just_list[100]", globals=globals(), number=1000000))         # взятие элемента списка 0.013246800001070369
print(timeit("collections_deque[100]", globals=globals(), number=1000000))  # взятие элемента deque 0.01606819999869913
"""
Вывод:

Замеры времени выполнения показали, что использование deque из модуля collections позволяет получить огромное 
преимущество перед классическим способом построения структуры данных дек. Особенно это проявляется, когда необходимо
добавить новый элемент в начало большого дека, скорость возрастает на множество порядков. К тому же значительно 
сокращается количество написанного кода. 

Получение элемента по индексу в collections.deque происходит медленнее чем при использовании классической структуры,
но это практически нивелируется, если увеличить количество вызовов.

При проведении измерений для классического дека сознательно использован собственный класс и вызовы объекта данного
класса, так как в реальной программе элементы дека не будут использоваться сами по себе, поэтому нет смысла измерять
скорость функций в отрыве от класса. Увеличение времени при частом обращении к методам объекта тоже является
показателем.

Таким образом, можно с уверенностью сказать, что collections.deque крайне полезен, нет никакой причины не использовать
его при построении дека. 
"""

