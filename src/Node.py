# -*- coding: utf-8 -*-
"""Class designed to create a stack."""


class Node(object):
    """Class designed to create node objects."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Method designed to create instances of Node class."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
