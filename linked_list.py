# -*- conding: utf-8 -*-
"""Create a linked list from scratch."""


class Node(object):
    """Node object to store data and pointer to next node within list."""

    def __init__(self, data=None, next_node=None):
        """Node constructor method."""
        self.data = data
        self.next_node = next_node


class Linked_List(object):
    """Linked list object to store a list of nodes."""

    def __init__(self, head=None, length=0):
        """Linked list constructor."""
        self.head = head
        self.length = length

    def insert(self, data):
        """Add a new node to the head of the linked list."""
        self.head = Node(data, self.head)
        self.length += 1

    def pop(self):
        """Remove and return the head of the linked list."""
        head = self.head
        self.head = head.next_node
        self.length = self.length - 1
        return head

    def size(self):
        """Return the length of the linked list."""
        return self.length

    def search(self, data):
        """Search for data and return the containing node."""
        node = self.head
        for i in range(self.length):
            if node.data == data:
                return node.data
            else:
                node = node.next_node

    def remove(self, data):
        """Remove specific node and patch link from prev to next."""
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
        """Display contents of list."""
        add_to = ")"
        node = self.head
        for i in range(self.length):
            add_to = str(node.data) + add_to
            if node.next_node:
                add_to = ', ' + add_to
            node = node.next_node
        add_to = '(' + add_to
        return add_to
