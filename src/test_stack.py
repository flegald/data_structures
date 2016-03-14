# -*- coding: utf-8 -*-
"""Tests for stack module."""

data = ['123', '456', '789']


def test_Node():
    """Test node module init method."""
    from stack import Node
    assert isinstance(Node(data[0]), Node)


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
