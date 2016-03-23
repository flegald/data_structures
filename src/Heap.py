#  _*_coding:utf-8 _*_
"""Create a heap data structure."""
from __future__ import division
import math


class Heap(object):
    """Create a heap data structure."""

    def __init__(self, val=()):
        """Init method for Heap class."""
        self.heap_list = []
        for item in val:
            self.heap_list.append(item)
        self.heap_list.sort()

    def push(self, val):
        """Add new node to heap."""
        self.heap_list.append(val)
        cursor = len(self.heap_list) + 1
        while (cursor // 2) > 0:
            if self.heap_list[cursor] < self.heap_list[cursor // 2]:
                holder = self.heap_list[cursor // 2]
                self.heap_list[cursor] = self.heap_list[cursor]
                self.heap_list[cursor] = holder
            cursor = cursor // 2
