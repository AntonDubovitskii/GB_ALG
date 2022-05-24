"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

import hashlib


def count_substrings(selected_str):
    control_set = set()
    info_list = []

    for i in range(len(selected_str)):
        for j in range(i + 1, len(selected_str) + 1):
            if selected_str[i:j] == selected_str:
                continue
            control_set.add(hashlib.md5(selected_str[i:j].encode('utf-8')).hexdigest())
            info_list.append(selected_str[i:j])

    print(info_list)
    print(control_set)
    return len(control_set)


print(count_substrings('papa'))
print(count_substrings('village'))

