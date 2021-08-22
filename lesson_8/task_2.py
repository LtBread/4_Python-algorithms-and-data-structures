"""2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

"""
from collections import Counter


def get_frequency(string):
    """
    Создает словарь частот повторения символов в строке
    :param string:
    :return: freque_dict

    """
    freque_dict = dict(Counter(string))
    return freque_dict


class Node:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self, freque_dict):
        self.leaf = [Node(k, v) for k, v in freque_dict.items()]
        while len(self.leaf) != 1:
            self.leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.leaf[-1].value + self.leaf[-2].value))
            n.left = self.leaf.pop(-1)
            n.right = self.leaf.pop(-1)
            self.leaf.append(n)
        self.root = self.leaf[0]
        self.buffer = list(range(10))

    def generate(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print(f'{node.name} = ', end='')
            for i in range(length):
                print(self.buffer[i], end='')
            print()
            return
        self.buffer[length] = 0
        self.generate(node.left, length + 1)
        self.buffer[length] = 1
        self.generate(node.right, length + 1)

    def encode(self):
        self.generate(self.root, 0)


if __name__ == '__main__':
    user_string = 'перовое второе третье'
    matrix = get_frequency(user_string)
    tree = HuffmanTree(matrix)
    tree.encode()
