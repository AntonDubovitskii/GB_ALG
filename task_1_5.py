"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
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


if __name__ == '__main__':
    PS_OBJ = PlatesStack(7)

    print(PS_OBJ.is_empty())
    PS_OBJ.plates_count()

    PS_OBJ.push_in(13)

    print(PS_OBJ.is_empty())
    PS_OBJ.plates_count()

    PS_OBJ.push_in(10)

    PS_OBJ.plates_count()

    PS_OBJ.take_plate(2, 2)

    PS_OBJ.pop_out(9)

    PS_OBJ.plates_count()

    PS_OBJ.pop_out(100)
    PS_OBJ.plates_count()

