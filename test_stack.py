# -*- coding: utf-8 -*-
"""Tests for stack module."""

data = ['123', '456', '789']


def test_Node():
    """Test node module init method."""
    from stack import Node
    assert isinstance(Node(data[0]), Node)


def test_set_data():
    """Test node module set data method."""
    from stack import Node
    test_node = Node(data[0])
    test_node.set_data(data[1])
    assert test_node.data == data[1]


def test_set_next():
    """Test node module set next method."""
    from stack import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node1.set_next(test_node2)
    assert test_node1.next_node == test_node2


def test_get_data():
    """Test node module get data method."""
    from stack import Node
    test_node = Node(data[0])
    assert test_node.get_data() == data[0]


def test_get_next_node():
    """Test node module get next method."""
    from stack import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node1.set_next(test_node2)
    assert test_node1.get_next_node() == test_node2


def test_Stack():
    """Test for stack init method."""
    from stack import Stack
    assert isinstance(Stack(), Stack)


def test_push():
    """Test stack push method."""
    from stack import Stack
    from stack import Node
    stack = Stack()
    stack.push(data[0])
    assert isinstance(stack.head, Node)


def test_pop():
    """Test stack pop method."""
    from stack import Stack
    stack = Stack()
    stack.push(data[0])
    assert stack.pop().data == data[0]


def test_pop_empty():
    """Test stack pop method."""
    from stack import Stack
    stack = Stack()
    assert stack.pop() is None
