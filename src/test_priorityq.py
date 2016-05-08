# -*- coding: utf-8 -*-
"""Prioityq tests."""
import pytest


def test_insert():
    """Test insert method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert('Value', 1)
    assert pq.dict[1] == ['Value']


def test_pop_empty():
    """Test pop from empty PQ raises index error."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_pop():
    """Test pop method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert('Value', 1)
    assert pq.pop() == ('Value')


def test_pop_multiple():
    """Test correct value is returned from a longer PQ."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert('ValueOne', 1)
    pq.insert('ValueTwo', 2)
    pq.insert('ValueThree', 3)
    assert pq.pop() == "ValueOne"


def test_peek_empty():
    """Test peek from empty PQ raises index error."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()


def test_peek():
    """Test peek method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert('Value', 1)
    assert pq.peek() == "Value"


def test_peek_multiple():
    """Test correct value is shown with a PQ of multiple values."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert('ValueOne', 1)
    pq.insert('ValueTwo', 2)
    pq.insert('ValueThree', 3)
    assert pq.peek() == "ValueOne"

