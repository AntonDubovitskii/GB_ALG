"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class WrongTreeValueException(TypeError):
    def __init__(self, txt):
        self.txt = txt


class MissingNodeExeption(AttributeError):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def _insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def _insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def insert_to_tree(self, value):
        try:
            if type(value) != int:
                raise WrongTreeValueException('Попытка добавить некорректное значение')
            if value > self.root:
                self._insert_right(value)
            elif value < self.root:
                self._insert_left(value)
        except WrongTreeValueException:
            print("Ошибка, введите число!")

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            if not self.right_child:
                raise MissingNodeExeption('Попытка обратиться к несуществующему потомку')
            return self.right_child
        except MissingNodeExeption:
            return f'Ошибка! У узла со значением {self.get_root_val()} отсутствует правый потомок!'

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            if not self.left_child:
                raise MissingNodeExeption('Попытка обратиться к несуществующему потомку')
            return self.left_child
        except MissingNodeExeption:
            return f'Ошибка! У узла со значением {self.get_root_val()} отсутствует левый потомок!'

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(50)

r.insert_to_tree(60)
r.insert_to_tree(45)

print(r.get_left_child())
print(r.get_left_child().get_root_val())

print(r.get_right_child())
print(r.get_right_child().get_root_val())

"""
Добавлен метод insert_to_tree(), автоматически определяющий, в каком положении должен быть потомок с таким значением.
Методы insert_right() и insert_left() сделаны приватными. 
Добавлена валидация переданных значений и обращений к отсутствующим узлам дерева.
"""
