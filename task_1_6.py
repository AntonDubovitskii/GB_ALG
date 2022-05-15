"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях.
"""


class Task:
    def __init__(self, description: str, work_done: bool):
        self.description = description
        self.work_done = work_done

    def work_hard(self):
        self.work_done = True


class TaskBoard:
    def __init__(self):
        self.base_queue = []
        self.rework_queue = []
        self.complete_queue = []

    def to_base_queue(self, obj: Task):
        if type(obj) == Task:
            self.base_queue.insert(0, obj)
            print(f'{self.base_queue[0].description} - добавлен в основную очередь задач')
        else:
            print('В очередь нельзя добавлять что попало! Сформируйте задачу по образцу')

    def is_empty_base(self):
        return True if self.base_queue == [] else False

    def is_empty_rework(self):
        return True if self.rework_queue == [] else False

    def is_empty_complete(self):
        return True if self.complete_queue == [] else False

    def from_base_queue(self):
        if self.is_empty_base():
            print('Очередь пуста')
        else:
            if self.base_queue[-1].work_done:
                self.complete_queue.insert(0, self.base_queue[-1])
                print(f'{self.base_queue[-1].description} - отправлен в список решенных задач')
            else:
                self.rework_queue.insert(0, self.base_queue[-1])
                print(f'{self.base_queue[-1].description} - отправлен в очередь задач на доработку')
            self.base_queue.pop()

    def show_content_base(self):
        print(f'-' * 100 + '\nЗадачи в главной очереди:\n')
        if self.is_empty_base():
            print('Очередь задач пуста!')
        else:
            for i in range(len(self.base_queue)):
                print(self.base_queue[i].description)
        print('-' * 100)

    def show_content_rework(self):
        print(f'-' * 100 + '\nЗадачи в очереди на доработку:\n')
        if self.is_empty_rework():
            print('Очередь задач пуста!')
        else:
            for i in range(len(self.rework_queue)):
                print(self.rework_queue[i].description)
        print('-' * 100)

    def show_content_complete(self):
        print(f'-' * 100 + '\nCписок выполненных задач:\n')
        if self.is_empty_complete():
            print('Очередь задач пуста!')
        else:
            for i in range(len(self.complete_queue)):
                print(self.complete_queue[i].description)
        print('-' * 100)


if __name__ == '__main__':

    meeting = Task('Провести совещание', True)
    drink_coffee = Task('Очень важное занятие', True)
    watch_youtube = Task('Никто не узнает', True)
    submit_report = Task('Квартальный отчет сам себя не составит', False)
    relax = Task('Отдых важен', True)

    new_taskboard = TaskBoard()

    new_taskboard.to_base_queue(meeting)
    new_taskboard.to_base_queue(drink_coffee)
    new_taskboard.to_base_queue(watch_youtube)
    new_taskboard.to_base_queue(submit_report)
    new_taskboard.to_base_queue(relax)
    new_taskboard.to_base_queue(1)

    new_taskboard.show_content_base()

    new_taskboard.from_base_queue()
    new_taskboard.from_base_queue()
    new_taskboard.from_base_queue()
    new_taskboard.from_base_queue()
    new_taskboard.from_base_queue()
    new_taskboard.from_base_queue()

    new_taskboard.show_content_rework()
    new_taskboard.show_content_complete()
    new_taskboard.show_content_base()

