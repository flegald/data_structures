# -*- coding: utf-8 -*-
"""Prioityq Class."""


class PriorityQueue:
    """PQ data structure class."""

    def __init__(self):
        """Priority Queue constructor method."""
        self.dict = {}

    def insert(self, value, priority):
        """Priority Queue insert method."""
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer")
        if priority in self.dict:
            self.dict[priority].append(value)
        else:
            self.dict[priority] = [value]
        print(self.dict)

    def pop(self):
        """Priority Queue pop method."""
        if len(self.dict):
            cursor = 0
            while cursor not in self.dict:
                cursor += 1
            next_node = self.dict[cursor][0]
            self.dict[cursor] = self.dict[cursor][1:]
            return next_node
        else:
            raise IndexError("The Priority Queue is empty")

    def peek(self):
        """Priority Queue peek method."""
        if len(self.dict):
            mostest_importantestest = self.dict[min(self.dict.keys())][0]
            return mostest_importantestest
        else:
            raise IndexError('The Priority Queue is empty')
