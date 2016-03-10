#  _*_ coding:utf-8 _*_
"""A module to create a queue data structure."""
from Node import Node


class Queue(object):
    """Queue data structure object creator."""

    def __init__(self, head=None, tail=None):
        """Queue object constructor."""
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, data):
        """Enqueue method for Queue object."""
        self.head = Node(data, self.head)
        if self.tail is None:
            self.tail = self.head
        else:
            self.head.next_node.prev_node = self.head
        self.length += 1

    def dequeue(self):
        """Dequeue method for Queue object."""
        old_tail = self.tail
        self.tail = self.tail.prev_node
        self.length -= 1
        return old_tail.data

    def peek(self):
        """Peek method for Queue object."""
        try:
            return self.tail.prev_node.data
        except AttributeError:
            return None

    def size(self):
        """Size method for Queue object."""
        return self.length
