# -*- coding: utf-8 -*-
import pytest
"""Test file for Deque list data structure."""

data = ['123', '234', '345']


def test_deque():
    """Test Deque class constructor."""
    from deque import Deque
    assert isinstance(Deque(), Deque)


def test_append():
    """Test Deque class append method."""
    from deque import Deque
    deque = Deque()
    deque.append(data[0])
    deque.append(data[1])
    assert deque.head.data == data[1]


def test_append_left():
    """Test Deque class append_left method."""
    from deque import Deque
    deque = Deque()
    deque.append_left(data[0])
    deque.append_left(data[1])
    assert deque.tail.data == data[1]


def test_pop():
    """Test Deque class pop method."""
    from deque import Deque
    deque = Deque()
    deque.append(data[0])
    deque.append(data[1])
    assert deque.pop() == data[1]
    assert deque.head.data == data[0]


def test_pop_left():
    """Test Deque class pop_left method."""
    from deque import Deque
    deque = Deque()
    deque.append(data[0])
    deque.append(data[1])
    assert deque.pop_left() == data[0]
    assert deque.tail.data == data[1]


def test_peek():
    """Tetst peek method of deque."""
    from deque import Deque
    deque = Deque()
    deque.append(data[0])
    deque.append(data[1])
    assert deque.peek() == data[1]


def test_peek_left():
    """Test peek method of deque."""
    from deque import Deque
    deque = Deque()
    deque.append(data[0])
    deque.append(data[1])
    assert deque.peek_left() == data[0]


def test_size():
    """Test peek method of deque."""
    from deque import Deque
    deque = Deque()
    deque.append(data[0])
    deque.append(data[1])
    assert deque.size() == 2

# Testing empty deque


def test_empty_pop():
    """Test pop from empty returns error."""
    from deque import Deque
    deque = Deque()
    with pytest.raises(AttributeError):
        deque.pop()


def test_empty_pop_left():
    """Test that pop_left raises error."""
    from deque import Deque
    deque = Deque()
    with pytest.raises(AttributeError):
        deque.pop_left()
