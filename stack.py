# -*- coding: utf-8 -*-
"""Class designed to create a stack."""


class Node(object):
    """Class designed to create node objects."""

    def __init__(self, data=None, next_node=None):
        """Method designed to create instances of Node class."""
        self.data = data
        self.next_node = next_node

    def set_next(self, next_node):
        """Method designed to set next_node of Node object."""
        self.next_node = next_node

    def set_data(self, data):
        """Method designed to set data of Node object."""
        self.data = data

    def get_next_node(self):
        """Method designed to return next_node of Node object."""
        return self.next_node

    def get_data(self):
        """Method designed to return data of Node object."""
        return self.data


class Stack(object):
    """Class designed to create stack objects."""

    def __init__(self, head=None):
        """Method designed to create instances of Stack class."""
        self.head = head

    def push(self, data):
        """Method designed to add node to the top of stack."""
        self.head = Node(data, self.head)

    def pop(self):
        """Method designed to remove and return head of stack."""
        try:
            head = self.head
            self.head = head.next_node
            return head
        except:
            return None
