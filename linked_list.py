# -*- conding: utf-8 -*-
"""TODO: Docstring."""


class Node(object):
    """TODO: Docstring."""

    def __init__(self, data=None, next_node=None):
        """TODO: Docstring."""
        self.data = data
        self.next_node = next_node

    def set_next(self, next):
        """TODO: Docstring."""
        self.next_node = next

    def get_data(self):
        """TODO: Docstring."""
        return self.data

    def get_next(self):
        """TODO: Docstring."""
        return self.next_node

    def set_data(self, data):
        """TODO: Docstring."""
        self.data = data


class Linked_List(object):
    """TODO: Docstring."""

    def __init__(self, head=None, length=0):
        """TODO: Docstring."""
        self.head = head
        self.length = length

    def insert(self, data):
        """TODO: Docstring."""
        self.head = Node(data, self.head)
        self.length += 1

    def pop(self):
        """TODO: Docstring."""
        old_head = self.head
        self.head = old_head.next_node
        self.length = self.length - 1
        return old_head

    def size(self):
        """TODO: Docstring."""
        return self.length

    def search(self, data):
        """TODO: Docstring."""
        node = self.head
        for i in range(self.length):
            if node.data == data:
                return node.data
            else:
                node = node.next_node

    def remove(self, data):
        """TODO: Docstring."""
        node = self.head
        node_prev = None
        for i in range(self.length):
            if node.data == data:
                if node_prev:
                    node_prev.next_node = node
                else:
                    self.head = self.head.next_node
                self.length = self.length - 1
                break
            else:
                node_prev = node
                node = node.next_node

    def display(self):
        """TODO: Docstring."""
        add_to = ")"
        node = self.head
        for i in range(self.length):
            add_to = str(node.data) + add_to
            if node.next_node:
                add_to = ', ' + add_to
            node = node.next_node
        add_to = '(' + add_to
        return add_to
