# -*- coding: utf-8 -*-
"""Class designed to create a stack."""


class Node(object):
    """Class designed to create node objects."""

    def __init__(self, data=None, next_node=None):
        """Method designed to create instances of Node class."""
        self.data = data
        self.next_node = next_node


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
