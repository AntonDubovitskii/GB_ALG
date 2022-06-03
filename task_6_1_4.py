
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

Это файл для четвертого скрипта
"""
from memory_profiler import memory_usage

"""
Для оптимизации взят один из вариантов, написанных для упражнения 1, ДЗ4 текущего курса.
Скрипт позволяет сохранить в массиве индексы четных элементов другого массива.
"""
nums = [el for el in range(1000000)]


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return res, mem_diff
    return wrapper


@decor
def func_3(nums):
    """
    Лямбда выражение и функция filter()
    """
    new_arr = list(filter(lambda x: (x % 2 == 0), nums))
    return new_arr


@decor
def func_3_gen(num):
    """
    Применение генератора
    """
    yield [number for number in num if number % 2 == 0]


if __name__ == '__main__':

    res, mem_diff = func_3(nums)
    print(f'Выполнение заняло {mem_diff} Mib')

    generator, mem_diff_gen = func_3_gen(nums)
    print(f'Выполнение заняло {mem_diff_gen} Mib')


"""
Применение генератора, отдающего значения последовательно, обеспечивает очень большую экономию памяти, по сравнению с 
обычным заполнением списка нужными значениями. Разница тем больше, чем больше значений необходимо обработать.
"""
