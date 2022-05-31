"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""


class HexCalc:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def hex_to_dec(number_string):
        return int(''.join(number_string), 16)

    def __add__(self, other):
        sum_dec = self.hex_to_dec(self.number) + self.hex_to_dec(other.number)
        return hex(sum_dec).replace('0x', '').upper()

    def __mul__(self, other):
        mul_dec = self.hex_to_dec(self.number) * self.hex_to_dec(other.number)
        return hex(mul_dec).replace('0x', '').upper()


hex_number_1 = list(input('Первое число: '))
hex_number_2 = list(input('Второе число: '))

print(hex_number_1)
print(hex_number_2)

hex_obj_1 = HexCalc(hex_number_1)
hex_obj_2 = HexCalc(hex_number_2)

print(f'Сумма чисел: {(hex_obj_1 + hex_obj_2)}')
print(f'Произведение чисел: {(hex_obj_1 * hex_obj_2)}')

