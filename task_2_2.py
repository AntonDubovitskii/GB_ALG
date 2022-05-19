"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_and_odd(my_number, even=0, odd=0):
    if my_number != 0:
        remainder = my_number % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_and_odd(my_number // 10, even, odd)
    else:
        print(f'Количество четных цифр во введенном числе - {even}, нечетных - {odd}')


number = int(input('Введите число для подсчета четных и нечетных цифр: \n'))
even_and_odd(number)
