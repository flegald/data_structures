# -*- conding: utf-8 -*-
"""Test queue module."""

data = [1, 2, 3, 4]


def test_queue():
    """Test instantiate queue."""
    from Queue import Queue
    assert isinstance(Queue(), Queue)


def test_enqueue():
    """Test enqueue method."""
    from Queue import Queue
    q = Queue()
    q.enqueue(data[0])
    assert q.head.data == data[0]


def test_dequeue():
    """Test dequeue method."""
    from Queue import Queue
    q = Queue()
    q.enqueue(data[0])
    q.enqueue(data[1])
    assert q.dequeue() == data[0]


def test_peek():
    """Test peek method."""
    from Queue import Queue
    q = Queue()
    q.enqueue(data[0])
    q.enqueue(data[1])
    assert q.peek() == data[1]


def test_size():
    """Test size method."""
    from Queue import Queue
    q = Queue()
    q.enqueue(data[0])
    q.enqueue(data[1])
    assert q.size() == 2
