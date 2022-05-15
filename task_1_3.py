"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company_info_dict = {'Walmart': 571960, 'Apple': 365820, 'UnitedHealth Group': 279320, 'Chevron': 135140,
                     'Daimler': 188440, 'Toyota': 291560}


def highest_income(info: dict):

    result_list = sorted(info, key=info.get, reverse=True)[:3]                                           # O(NlogN)
    result_dict = {result_list[0]: info.get(result_list[0]), result_list[1]: info.get(result_list[1]),
                   result_list[2]: info.get(result_list[2])}                                             # O(1)
    return result_dict                                                                                   # 0(1)


print(highest_income(company_info_dict))
