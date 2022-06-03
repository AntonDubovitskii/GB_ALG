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
def func_2_base(nums):
    """
    List comprehension
    """
    return [i for i in nums if i % 2 == 0]


@memory
def func_2_base_filter(nums):
    """
    List comprehension
    """
    return filter(lambda x: x % 2 == 0, nums)


my_list = [el for el in range(1000000000)]

if __name__ == '__main__':
    func_2_base(my_list)  # Выполнение заняло 12255.8203125 Mib
    func_2_base_filter(my_list)  # Выполнение заняло 0.26171875 Mib

"""
Замена List comprehension на функцию filter() с лямбда выражением, для обозначения условия, позволяет сильно уменьшить
потребляемую память.
"""

