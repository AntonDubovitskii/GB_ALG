"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""


def series_elements_sum(el_amount, counter=0, el=1.0, el_sum=0.0):
    if counter < el_amount:
        return series_elements_sum(el_amount, counter + 1, el/(-2), el_sum + el)
    else:
        return f'Количество элементов {el_amount}, их сумма {el_sum}'


required_amount = int(input('Введите количество элементов: '))
print(series_elements_sum(required_amount))

