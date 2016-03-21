#  _*_coding:utf-8 _*_
"""Create a heap data structure."""
from __future__ import division
import math


class Heap(object):
    """Create a heap data structure."""

    def __init__(self):
        """Init method for Heap class."""
        self.hl = []

    def get_parent(self, idx):
        """Get index number of Node's parent."""
        return (idx - 1) // (2)

    def get_left(self, idx):
        """Get left child."""
        return 2 * idx + 1

    def get_right(self, idx):
        """Get right child."""
        return 2 * idx + 2

    def compare_parent(self, idx):
        """Compare node it parent."""
        while True:
            left = self.get_left(idx)
            right = self.get_right(idx)
            if left <= len(self.hl) and self.hl[left] > self.hl[idx]:
                largest = left
            else:
                largest = idx
            if right <= len(self.hl) and self.hl[right] > self.hl[largest]:
                largest = right
            if largest != idx:
                temp = self.hl[idx]
                self.hl[idx] = self.hl[largest]
                self.hl[largest] = temp
            else:
                break

    def push(self, val):
        """Add new node to heap."""
        self.hl.append(val)
        try:
            self.compare_parent(self.hl.index(self.hl[-1]))
        except (ValueError, IndexError):
            pass

    def pop(self):
        """Remove top item of heap."""
        temp = self.hl.pop(0)
        self.compare_parent(self.hl.index(self.hl[-1]))
        return temp
