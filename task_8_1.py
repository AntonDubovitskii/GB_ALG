"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


class HaffmanCoding:
    def __init__(self, text: str):
        self.text = text
        self.code_table = {}
        self.encoding(self.building_tree())

    def count_and_sort(self):
        value_count = Counter(self.text)
        sorted_elements = deque(sorted(value_count.items(), key=lambda item: item[1]))
        return sorted_elements

    def building_tree(self):
        elements = self.count_and_sort()
        if len(elements) != 1:
            while len(elements) > 1:
                weight = elements[0][1] + elements[1][1]
                new_elem = {0: elements.popleft()[0],
                            1: elements.popleft()[0]}
                for i, _count in enumerate(elements):
                    if weight > _count[1]:
                        continue
                    else:
                        elements.insert(i, (new_elem, weight))
                        break
                else:
                    elements.append((new_elem, weight))
        else:
            weight = elements[0][1]
            new_elem = {0: elements.popleft()[0], 1: None}
            elements.append((new_elem, weight))
        return elements[0][0]

    def encoding(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.encoding(tree[0], path=f'{path}0')
            self.encoding(tree[1], path=f'{path}1')

    def get_string_code(self):
            result = ''
            for symbol in self.text:
                result += self.code_table[symbol]
            return result


if __name__ == '__main__':
    my_string = input("Введите строку: ")                    # Введите строку: На дворе трава

    cls = HaffmanCoding(my_string)

    print(f'Построенное дерево: {cls.building_tree()}')
    # Построенное дерево: {0: {0: {0: 'т', 1: {0: 'о', 1: 'е'}}, 1: 'а'},
    # 1: {0: {0: 'в', 1: 'р'}, 1: {0: {0: 'Н', 1: 'д'}, 1: ' '}}}
    print(f'Закодированный текст: {cls.get_string_code()}')
    # Закодированный текст: 1100011111101100001010100111110001010110001
