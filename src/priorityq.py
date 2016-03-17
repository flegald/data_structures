# -*- coding: utf-8 -*-
"""Prioityq Class."""


class PriorityQueue:
    """PQ data structure class."""

    def __init__(self):
        """Priority Queue constructor method."""
        self.dict = {}

    def insert(self, key, val):
        """Priority Queue insert method."""
        self.dict.setdefault(key, []).append(val)

    def pop(self):
        """Priority Queue pop method."""
        mostest_importantestest = self.dict[min(self.dict.keys())][0]
        if min(self.dict.keys()) < 0:
            self.dict[min(self.dict.keys())].pop
        return mostest_importantestest

    def peek(self):
        """Priority Queue peek method."""
        mostest_importantestest = self.dict[min(self.dict.keys())][0]
        return mostest_importantestest
