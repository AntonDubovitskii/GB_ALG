"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def number_flip(number):
    integer_part, remainder = divmod(number, 10)

    if integer_part == 0:
        return str(remainder)
    else:
        return str(remainder) + str(number_flip(integer_part))


def number_flip_old(number):
    """
    Моё первоначальное решение, до того как я узнал о функции divmod() на вебинаре. Решил тоже оставить :)
    """
    remainder = number % 10
    number //= 10

    if number == 0:
        return str(remainder)
    else:
        return str(remainder) + str(number_flip_old(number))


my_number = int(input('Введите число, которое требуется перевернуть: '))
print(number_flip(my_number))
print(number_flip_old(my_number))

