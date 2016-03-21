#  _*_coding:utf-8 _*_
"""Test create a heap data structure."""

data = [1, 2, 3, 4]


def heap_init():
    """Test heap init."""
    from Heap import Heap
    assert isinstance(Heap() == Heap)


def test_push():
    """Test push method."""
    from Heap import Heap
    hl = Heap()
    hl.push(data[0])
    hl.push(data[1])
    assert hl.hl[1] == data[1]


def test_get_parent():
    """Test get_parent method."""
    from Heap import Heap
    hl = Heap()
    hl.hl.append(data[0])
    hl.hl.append(data[1])
    hl.hl.append(data[2])
    assert hl.hl[hl.get_parent(1)] == data[0]
    assert hl.hl[hl.get_parent(2)] == data[0]


def test_get_left():
    """Test get_left method."""
    from Heap import Heap
    hl = Heap()
    hl.push(data[0])
    hl.push(data[1])
    hl.push(data[2])
    assert hl.hl[hl.get_left(0)] == data[1]


def test_get_right():
    """Test get_left method."""
    from Heap import Heap
    hl = Heap()
    hl.push(data[0])
    hl.push(data[1])
    hl.push(data[2])
    assert hl.hl[hl.get_right(0)] == data[2]


def test_compare_parent():
    """Test get_left method."""
    from Heap import Heap
    hl = Heap()
    hl.push(data[2])
    hl.push(data[1])
    hl.push(data[3])
    hl.compare_parent(0) 
    assert hl.hl == [data[3], data[1], data[2]]


def test_pop():
    """Test pop method."""
    from Heap import Heap
    hl = Heap()
    hl.push(data[2])
    hl.push(data[1])
    hl.push(data[3])
    assert hl.pop() == data[2]

