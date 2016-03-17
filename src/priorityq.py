# -*- coding: utf-8 -*-
"""Prioityq Class."""


# dict of key (priority) : value (data) pairs
#
#
# IF THE LIST @ KEY IS EMPTY AFTER POPPING!
#
# if dict(min(dict.keys)) < 0 :
#       dict(min(dict.keys)).pop


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
        # keys = self.dict.keys()
        # min_key = min(keys)
        # highest = self.dict[min_key][0]
        mostest_importantestest = self.dict[min(self.dict.keys())][0]
        if min(self.dict.keys()) < 0:
            self.dict[min(self.dict.keys())].pop
        return mostest_importantestest
        # return highest

    def peek(self):
        """Priority Queue peek method."""
        mostest_importantestest = self.dict(min(self.dict.keys()))[0]
        return mostest_importantestest
