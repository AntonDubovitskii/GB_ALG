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

Это файл для первого скрипта
"""

from memory_profiler import profile
"""
Для оптимизации выбран скрипт из задания 1, ДЗ6 текущего курса.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
"""


@profile
def func_5():
    array = list(range(500000))
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


@profile
def func_5_no_garbage():
    array = list(range(500000))
    mydict = {}
    for i in array:
        dict_key = i
        if dict_key not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    del array
    result_key = max(mydict, key=mydict.get)
    detections_number = mydict[result_key]
    del mydict
    return f"Чаще всего встречается число {result_key}, оно появилось в массиве" \
           f" {detections_number} раз(а)"


func_5()             # 58.8 MiB
func_5_no_garbage()  # 22.0 MiB

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     22.0 MiB     22.0 MiB           1   @profile
    45                                         def func_5_no_garbage():
    46     38.8 MiB     16.8 MiB           1       array = list(range(500000))
    47     38.8 MiB      0.0 MiB           1       mydict = {}
    48     58.8 MiB      0.0 MiB      500001       for i in array:
    49     58.8 MiB      0.0 MiB      500000           dict_key = i
    50     58.8 MiB      0.0 MiB      500000           if dict_key not in mydict:
    51     58.8 MiB     20.0 MiB      500000               mydict[i] = 1
    52                                                 else:
    53                                                     mydict[i] += 1
    54     55.0 MiB     -3.8 MiB           1       del array
    55     55.0 MiB      0.0 MiB           1       result_key = max(mydict, key=mydict.get)
    56     55.0 MiB      0.0 MiB           1       detections_number = mydict[result_key]
    57     22.0 MiB    -33.0 MiB           1       del mydict
    58     22.0 MiB      0.0 MiB           2       return f"Чаще всего встречается число {result_key}, оно появилось в 
    массиве" \
    59     22.0 MiB      0.0 MiB           1              f" {detections_number} раз(а)"



Process finished with exit code 0

    
    
Вывод:
При выполнении функции func_5 используется 58.8 MiB оперативной памяти. При помощи команды del удалены ссылки на список 
array и словарь mydict, после того как они выполнили свою задачу, таким образом удалоось освободить 36.8 MiB памяти.
"""

