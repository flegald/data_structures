"""Implementation of Binary Search Tree."""
from collections import deque



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
        """Left property."""
        return self._left

    @left.setter
    def left(self, new_node):
        self._left = new_node
        if new_node is not None:
            new_node.parent = self

    @property
    def right(self):
        """Right property."""
        return self._right

    @right.setter
    def right(self, new_node):
        self._right = new_node
        if new_node is not None:
            new_node.parent = self

    def depth(self):
        """Return depth of the tree."""
        if not self.val:
            return 0
        elif not self.left and not self.right:
            return 1
        else:
            left_depth = self.left.depth() if self.left else 0
            right_depth = self.right.depth() if self.right else 0
            return max(left_depth, right_depth) + 1

    def in_order(self):
        """Yield items by in-order traversal."""
        if self.left:
            for item in self.left.in_order():
                yield item
        yield self.val
        if self.right:
            for item in self.right.in_order():
                yield item

    def pre_order(self):
        """Yield items by pre-order traversal."""
        yield self.val
        if self.left:
            for item in self.left.pre_order():
                yield item
        if self.right:
            for item in self.right.pre_order():
                yield item

    def post_order(self):
        """Yeild items by post-ordre traversal."""
        if self.left:
            for item in self.left.post_order():
                yield item
        if self.right:
            for item in self.right.post_order():
                yield item
        yield self.val


class Bst(object):
    """Binary Search Tree."""

    def __init__(self, root=None):
        """Init BST."""
        self.root = root
        self.size = 0

    def insert(self, val):
        """Insert into tree."""
        node = Node(val)
        if self.root is None:
            self.root = node
            self.size += 1
        else:
            current = self.root
            while True:
                if current.val == val:
                    break
                elif val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        self.size += 1
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        self.size += 1
                        break

    def contains(self, val):
        """Return if node is contained in bst."""
        if not self.root:
            return False
        current = self.root
        while True:
            if current.val == val:
                return True
            elif val < current.val:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False

    def size(self):
        """Return size of list."""
        return self.size

    def depth(self):
        """Return the number of levels in the tree."""
        if not self.root:
            return 0
        return self.root.depth()

    def balance(self):
        """Return how balanced the tree is."""
        if not self.root:
            return None
        counter = 0
        current = self.root

        while current.left:
            counter += 1
            current = current.left

        current = self.root

        while current.right:
            counter -= 1
            current = current.right

        return counter

    def in_order(self):
        """Yield items by in-order traversal."""
        if not self.root:
            return
        for item in self.root.in_order():
            yield item

    def pre_order(self):
        """Yield items by pre-order traversal."""
        if not self.root:
            return
        for item in self.root.pre_order():
            yield item

    def post_order(self):
        """Yield items by post-order traversal."""
        if not self.root:
            return
        for item in self.root.post_order():
            yield item

    def breadth_first(self):
        """Yield items by breadth-first traversal."""
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            current = queue.pop()
            yield current.val
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)


