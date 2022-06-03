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

Это файл для третьего скрипта
"""

from pympler import asizeof

"""
Реализация класса-структуры "стопка тарелок" из 5 задания 1 домашней работы. В целях лучшей наглядности, удалил
все методы данного класса, так как они здесь не используются.
"""


class PlatesStack:
    def __init__(self, max_plates):
        self.max_plates = max_plates
        self.all_plates = [[]]
        self.stack_number = 0
        self.plates_in_stack = 0

    def is_empty(self):
        return True if self.stack_number == 0 and self.plates_in_stack == 0 else False

    def push_in(self, plates_number):
        for plate in range(plates_number):
            if self.plates_in_stack == self.max_plates:
                self.stack_number += 1
                self.plates_in_stack = 0
                self.all_plates.append([])
            self.all_plates[self.stack_number].append(f'тарелка №'
                                                      f'{self.stack_number * self.max_plates + self.plates_in_stack}')
            self.plates_in_stack += 1

    def pop_out(self, plates_number):
        for plate in range(plates_number):
            if self.is_empty():
                print(f'Взяли {plate} тарелок, больше нет!')
                break
            elif self.plates_in_stack == 0:
                self.stack_number -= 1
                self.plates_in_stack = self.max_plates
            self.all_plates[self.stack_number].pop()
            self.plates_in_stack -= 1

    def plates_count(self):
        print(f'Прямо сейчас на столе {self.stack_number} полных стопок тарелок, '
              f'в последней стопке {self.plates_in_stack} тарелок')

    def take_plate(self, stack, plate):
        print(f'В руках {self.all_plates[stack][plate]}')


class PlatesStackSlots:
    __slots__ = ['max_plates', 'all_plates', 'stack_number', 'plates_in_stack']

    def __init__(self, max_plates):
        self.max_plates = max_plates
        self.all_plates = [[]]
        self.stack_number = 0
        self.plates_in_stack = 0

    def is_empty(self):
        return True if self.stack_number == 0 and self.plates_in_stack == 0 else False

    def push_in(self, plates_number):
        for plate in range(plates_number):
            if self.plates_in_stack == self.max_plates:
                self.stack_number += 1
                self.plates_in_stack = 0
                self.all_plates.append([])
            self.all_plates[self.stack_number].append(f'тарелка №'
                                                      f'{self.stack_number * self.max_plates + self.plates_in_stack}')
            self.plates_in_stack += 1

    def pop_out(self, plates_number):
        for plate in range(plates_number):
            if self.is_empty():
                print(f'Взяли {plate} тарелок, больше нет!')
                break
            elif self.plates_in_stack == 0:
                self.stack_number -= 1
                self.plates_in_stack = self.max_plates
            self.all_plates[self.stack_number].pop()
            self.plates_in_stack -= 1

    def plates_count(self):
        print(f'Прямо сейчас на столе {self.stack_number} полных стопок тарелок, '
              f'в последней стопке {self.plates_in_stack} тарелок')

    def take_plate(self, stack, plate):
        print(f'В руках {self.all_plates[stack][plate]}')


if __name__ == '__main__':
    PS_OBJ = PlatesStack(7)
    PS_OBJ_SLOTS = PlatesStackSlots(7)

    print(f'Размер изначального объекта, каким он был в моем дз№1: {asizeof.asizeof(PS_OBJ)}')
    print(f'Размер того же объекта, но оптимизированного при помощи slots: {asizeof.asizeof(PS_OBJ_SLOTS)}')

"""
Вывод:
При помощи слотов удалось уменьшить размер объекта более чем в 2 раза. В данном случае динамически добавлять новые 
атрибуты не требуется, поэтому данная оптимизация полностью уместна. 
"""