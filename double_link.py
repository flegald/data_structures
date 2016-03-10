#  _*_ coding: utf-8 _*__
"""Implement a double linked list data structure."""


class Node(object):
    """Create Node object."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Instantiate Node object."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class Double_Link(object):
    """Create Double List Object."""

    def __init__(self, head=None, tail=None):
        """Instantiate double link."""
        self.head = head
        self.tail = tail

    def insert(self, data):
        """Insert Node into head of list."""
        self.head = Node(data, self.head)
        if self.tail is None:
            self.tail = self.head
        else:
            self.head.next_node.prev_node = self.head

    def append(self, data):
        """Insert Node into tail of list."""
        self.tail = Node(data, None, self.tail)
        if self.head is None:
            self.head = self.tail
        else:
            self.tail.prev_node.next_node = self.tail

    def pop(self):
        """Remove and return head of list."""
        head = self.head
        self.head = head.next_node
        return head

    def shift(self):
        """Remove and return tail of list."""
        tail = self.tail
        self.tail = tail.prev_node
        return tail

    def remove(self, data):
        """Remove a specific Node from the list."""
        node = self.head
        try:
            while True:
                if node.data == data:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    elif node == self.head:
                        self.head = node.next_node
                    elif node == self.tail:
                        self.tail = node.prev_node
                    else:
                        node.next_node.prev_node = node.prev_node
                        node.prev_node.next_node = node.next_node
                    break
                else:
                    node = node.next_node
        except AttributeError:
            pass
