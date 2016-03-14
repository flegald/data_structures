# _*_ coding:utf-8 _*_
"""Create a deque data structure."""
from Node import Node


class Deque(object):
    """Create double list object."""

    def __init__(self, head=None, tail=None):
        """Instantiate double link."""
        self.head = head
        self.tail = tail
        self.length = 0

    def append_left(self, data):
        """Insert Node into head of list."""
        self.head = Node(data, self.head)
        self.length += 1

    def append(self, data):
        """Insert Node into tail of list."""
        self.tail = Node(data, None, self.tail)
        self.length += 1

    def pop(self):
        """Remove and return head of list."""
        head = self.head
        self.head = head.next_node
        self.length -= 1
        return head

    def pop_left(self):
        """Remove and return tail of list."""
        tail = self.tail
        self.tail = tail.prev_node
        self.length -= 1
        return tail

    def peek(self):
        """See adjacent Node's value."""
        try:
            return self.head.data
        except AttributeError:
            return None

    def peek_left(self):
        """See adjacent Node's value."""
        try:
            return self.tail.data
        except AttributeError:
            return None

    def size(self):
        """Get the size of the list."""
        return self.length
