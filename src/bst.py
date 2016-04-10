"""Binary Search Tree."""

class Node(object):

    def __init__(self, value):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value


class Bst(object):
    """Tree."""

    def __init__(self, root):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            