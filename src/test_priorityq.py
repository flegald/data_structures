# -*- coding: utf-8 -*-
"""Prioityq tests."""


DATA = [(1, 'one'), (0, 'zero'), (2, 'two')]


def test_insert():
    """Test insert method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert(*DATA[0])
    assert pq.dict[DATA[0][0]][0] == DATA[0][1]


def test_pop():
    """Test insert method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert(*DATA[0])
    assert pq.pop() == DATA[0][1]


def test_peek():
    """Test insert method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert(*DATA[0])
    assert pq.peek() == DATA[0][1]
