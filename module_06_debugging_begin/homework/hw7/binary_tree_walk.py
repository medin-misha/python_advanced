"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node == None:
            return node, parent, False

        elif value == node.data:
            return node, parent, True

        elif value < node.data and \
                node.left:
            return self.__find(node.left, node, value)

        elif value > node.data and \
                node.right:
            return self.__find(node.right, node, value)

        return node, parent, False
    def __delNode(self, node, parent):
        if parent.left == node:
            parent.left = None
        elif parent.right == None:
            parent.right = None
    def __delChildNode(self, node, parent):
        if parent.left == node :
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left
        if parent.right == node :
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left
    def __findMin(self, node, parent):
        if node.left:
            return self.__findMin(node.left, node)
        return node, parent

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        node, parent, isObj = self.__find(self.root, None, obj.data)
        if not isObj and node:
            if obj.data < node.data:
                node.left = obj
            elif obj.data > node.data:
                node.right = obj
    def delete(self, key):
        node, parent, isObest = self.__find(self.root, None, key)
        if not isObest:
            return None
        elif node.left == None and None:
            self.__delNode(node, parent)
        elif node.left is None or node.right is None:
            self.__delChildNode(node, parent)
        else:
            sr, pr = self.__findMin(node.right, node)
            node.data = sr.data
            self.__delChildNode(sr, pr)

    def show(self, node):
        if node is None:
            return None
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end = "           ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

NumbersList = [
    random.randint(1, 100000) for _ in range(100)
]
tree = Tree()
for number in NumbersList:
    tree.append(
        Node(number)
    )

tree.show(tree.root)