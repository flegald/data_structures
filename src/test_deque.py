# -*- coding: utf-8 -*-
"""Test file for Deque list data structure."""

data = ['123', '234', '345']


def test_deque():
    """Test Deque class constructor."""
    from deque import Deque
    assert isinstance(Deque(), Deque)


def test_append_left():
    """Test Deque class append_left method."""
    from deque import Deque
    dll = Deque()
    dll.append_left(data[0])
    dll.append_left(data[1])
    assert dll.head.data == data[1]


def test_append():
    """Test Deque class append method."""
    from deque import Deque
    dll = Deque()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.tail.data == data[1]


def test_pop():
    """Test Deque class pop method."""
    from deque import Deque
    dll = Deque()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.pop().data == data[1]


def test_pop_left():
    """Test Deque class pop_left method."""
    from deque import Deque
    dll = Deque()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.pop_left().data == data[1]


def test_peek():
    """Tetst peek method of deque."""
    from deque import Deque
    dll = Deque()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.peek() == '234'


def test_peek_left():
    """Test peek method of deque."""
    from deque import Deque
    dll = Deque()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.peek_left() == '123'


def test_size():
    """Test peek method of deque."""
    from deque import Deque
    dll = Deque()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.size() == 2
