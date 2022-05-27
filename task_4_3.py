"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    enter_num = str(enter_num)
    revers_num = ''
    num_length = len(str(enter_num))
    while num_length:
        num_length -= 1
        revers_num += enter_num[num_length]
    return revers_num


test_number = 790259589552888795213

print('-'*100)
print(f'Первая функция, с рекурсией, скорость выполнения: ')
print(timeit(f"revers({test_number})", globals=globals(), number=1000000))      # 2.1221867999993265

print('-'*100)
print(f'Вторая функция, с циклом while, скорость выполнения: ')
print(timeit(f"revers_2({test_number})", globals=globals(), number=1000000))    # 1.3433806000030017

print('-'*100)
print(f'Третья функция, с применением срезов, скорость выполнения: ')
print(timeit(f"revers_3({test_number})", globals=globals(), number=1000000))    # 0.1445088999971631

print('-'*100)
print(f'Третья функция, с применением функции reversed(), скорость выполнения: ')
print(timeit(f"revers_4({test_number})", globals=globals(), number=1000000))    # 0.39159010000003036

print('-'*100)
print(f'Третья функция, c копированием из строки в строку поэлементно при помощи цикла while, скорость выполнения: ')
print(timeit(f"revers_5({test_number})", globals=globals(), number=1000000))    # 0.984682199996314

"""
Вывод:

Наиболее эффективным алгоритмом оказался revers_3(), где для решения задачи были применены срезы. Отсутствие 
арифметических операций делает данный метод наиболее быстрым и оптимальным. 

На втором месте revers_4(),
где применена встроенная функция reversed(). Данная функция возвращает итератор, что позволяет также получить 
неплохую скорость выполнения задачи. 

На третьем месте revers_5(). В данном алгоритме не используются арифметические операции, но применяется
конкатенация строк, по сути результирующая строка строится заново на каждой итерации цикла. 

На четвертом месте revers_2(), где просто применяются арифметические действия и цикл. Как показывает профилирование, 
арифметических операций в подобных задачах следует избегать.

На пятом и последнем месте revers(), где не только применяются арифметические операции, но еще и рекурсия, что приводит
к очень сильной просадке в быстродействии - почти в 15 раз медленнее срезов. Подобный метод решения данной задачи
крайне не рекомендуется. 
"""

