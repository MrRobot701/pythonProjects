import random

from collection.heap import color_text


def isRoot(node):
    return node.parent is None


def isLeaf(node):
    return node.right is None and node.left is None


def validate(node):
    if node is None or isRoot(node): raise Exception("Can't rotate")


def validateIsLeft(node):
    validate(node)
    if node.parent.left != node: raise Exception("Can't right rotate not left child")


def validateIsRight(node):
    validate(node)
    if node.parent.right != node: raise Exception("Can't left rotate not right child")


def randomizedTreap(): return RandomizedTreap()


class Treap:

    def __init__(self):
        self.root = None

    def rightRotate(self, node):
        validateIsLeft(node)
        parent = node.parent
        self.updateGrandparent(node)
        parent.setLeft(node.right)
        node.setRight(parent)

    def leftRotate(self, node):
        validateIsRight(node)
        parent = node.parent
        self.updateGrandparent(node)
        parent.setRight(node.left)
        node.setLeft(parent)

    def updateGrandparent(self, node):
        grandparent = node.parent.parent
        if grandparent is not None:
            if grandparent.left == node.parent:
                grandparent.setLeft(node)
            elif grandparent.right == node.parent:
                grandparent.setRight(node)
            else:
                raise Exception("Treap is inconsistent state")
        else:
            self.root = node
            node.parent = None

    def search(self, node, key):
        if node is None: return
        if node.key == key:
            return node
        elif key < node.key:
            self.search(node.left, key)
        else:
            self.search(node.right, key)

    def insert(self, key, priority):
        node = self.root
        newNode = Node(key, priority)
        parent = None
        while node is not None:
            parent = node
            if node.key <= key:
                node = node.right
            else:
                node = node.left
        if parent is None:
            self.root = newNode
            return
        elif key <= parent.key:
            parent.left = newNode
        else:
            parent.right = newNode
        newNode.parent = parent
        while not isRoot(newNode) and newNode.priority < newNode.parent.priority:
            if newNode == newNode.parent.left:
                self.rightRotate(newNode)
            else:
                self.leftRotate(newNode)
        if isRoot(newNode): self.root = newNode

    def remove(self, key, printNode = False):
        node = self.search(self.root, key)
        if printNode: print(''.join(self.root.toString("", True, [], node)))
        if node is None: return False
        if isRoot(node) and isLeaf(node):
            self.root = None
            return True
        while not isLeaf(node):
            if node.left is not None and (node.right is None or node.left.priority < node.right.priority):
                self.rightRotate(node.left)
            else:
                self.leftRotate(node.right)
            if isRoot(node.parent): self.root = node.parent
            if printNode: print(''.join(self.root.toString("", True, [], node)))
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
        return True

    def __str__(self):
        return str(self.root)


class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None

    def setLeft(self, node):
        self.left = node
        if node: node.parent = self

    def setRight(self, node):
        self.right = node
        if node: node.parent = self

    def __str__(self):
        return ''.join(self.toString("", True, []))

    def toString(self, prefix, isTail, string, coloredNode=None):
        if self.right is not None:
            self.right.toString(f"{prefix}{'│   ' if isTail else '    '}", False, string, coloredNode)
        nodeText = f"({self.key}, {self.priority})"
        if self == coloredNode: nodeText = color_text(nodeText)
        string.append(f"{prefix}{'└── ' if isTail else '┌── '}{nodeText}\n")
        if self.left is not None:
            self.left.toString(f"{prefix}{'    ' if isTail else '│   '}", True, string, coloredNode)
        return string


class RandomizedTreap(Treap):

    def __init__(self):
        super().__init__()

    def insert(self, key, priority=None):
        super().insert(key, random.uniform(0, 1))
