"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
Это файл для второго скрипта
"""

from memory_profiler import memory_usage
from collections import defaultdict

"""
Скрипт из задания 1, ДЗ-5, текущего курса.
Программа определяет среднюю прибыль (за год для всех предприятий)
и выводит наименования предприятий, чья прибыль выше среднего и отдельно наименования предприятий,
чья прибыль ниже среднего
"""

def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
def income_comparison():
    companies_count = int(input('Введите количество компаний, которые будут рассматриваться: '))
    companies_dict = defaultdict(list)

    for i in range(companies_count):
        company_name = input('Введите название предприятия: ')

        try:
            profit = [int(x) for x in input('Через пробел введите прибыль компании за '
                                            'каждый квартал этого года: ').split(' ')]
            companies_dict[company_name] = sum(profit)
        except ValueError:
            print('Ошибка! Допускается вводить только числа через пробел!')

    try:
        average_profit = sum(companies_dict.values()) / len(companies_dict.values())

        print(f'Средняя годовая прибыль всех компаний: {average_profit}')

        print(f'Компании с прибылью выше среднего значения: '
              f'{list({key: value for (key, value) in companies_dict.items() if value > average_profit})}')
        print(f'Компании с прибылью ниже среднего значения: '
              f'{list({key: value for (key, value) in companies_dict.items() if value < average_profit})}')
    except ZeroDivisionError:
        print('Ошибка! Не получено данных ни об одной компании!')


@memory
def income_comparison_map():
    companies_count = int(input('Введите количество компаний, которые будут рассматриваться: '))
    companies_dict = defaultdict(list)

    for i in range(companies_count):
        company_name = input('Введите название предприятия: ')

        try:
            profit = map(int, input('Через пробел введите прибыль компании за '
                                            'каждый квартал этого года: ').split(' '))
            companies_dict[company_name] = sum(profit)
        except ValueError:
            print('Ошибка! Допускается вводить только числа через пробел!')

    try:
        average_profit = sum(companies_dict.values()) / len(companies_dict.values())

        print(f'Средняя годовая прибыль всех компаний: {average_profit}')

        print(f'Компании с прибылью выше среднего значения: '
              f'{list({key: value for (key, value) in companies_dict.items() if value > average_profit})}')
        print(f'Компании с прибылью ниже среднего значения: '
              f'{list({key: value for (key, value) in companies_dict.items() if value < average_profit})}')
    except ZeroDivisionError:
        print('Ошибка! Не получено данных ни об одной компании!')


income_comparison()  # Выполнение заняло 0.0625 Mib
income_comparison_map()  # Выполнение заняло 0.05859375 Mib

"""
Введите количество компаний, которые будут рассматриваться: 5
Введите название предприятия: 1
Через пробел введите прибыль компании за каждый квартал этого года: 8239487234 82347982347 82374892374 832479283
Введите название предприятия: 2
Через пробел введите прибыль компании за каждый квартал этого года: 28349237489 423847239847 98273498237498 82374892347
Введите название предприятия: 3
Через пробел введите прибыль компании за каждый квартал этого года: 8234923798478 28347923847 2834793827489 
4823974923874
Введите название предприятия: 4
Через пробел введите прибыль компании за каждый квартал этого года: 823479823749 28347923845723987 4823749823749823 
48273489237498
Введите название предприятия: 5
Через пробел введите прибыль компании за каждый квартал этого года: 823497823984 48923748237498237498 48237498237498237 
4849283479283479
Средняя годовая прибыль всех компаний: 9.80203430345126e+18
"""

"""
Вывод:

Применение функции map() вместо конструкции int(x) for x in, позволило получить небольшую экономию памяти.
"""