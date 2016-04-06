"""Implementation of Binary Search Tree."""


class Node(object):
    """Binary Search Tree."""

    def __init__(self, val=None, left=None, right=None, parent=None):
        """Initialize BST."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, new_node):
        self._left = new_node
        if new_node is not None:
            new_node.parent = self

