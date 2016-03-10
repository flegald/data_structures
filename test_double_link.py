# -*- coding: utf-8 -*-
"""Test file for double_linked list data structure."""

data = ['123', '234', '345']


def test_node():
    """Test node class init method."""
    from double_link import Node
    assert isinstance(Node(data[0]), Node)


def test_set_data():
    """Test node class set data method."""
    from double_link import Node
    test_node = Node(data[0])
    test_node.set_data(data[1])
    assert test_node.data == data[1]


def test_set_next():
    """Test node class set next method."""
    from double_link import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node1.set_next(test_node2)
    assert test_node1.next_node == test_node2


def test_set_prev():
    """Test node class set prev method."""
    from double_link import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node2.set_prev(test_node1)
    assert test_node2.prev_node == test_node1


def test_get_data():
    """Test node class get data method."""
    from double_link import Node
    test_node = Node(data[0])
    assert test_node.get_data() == data[0]


def test_get_next():
    """Test node class get next method."""
    from double_link import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node1.set_next(test_node2)
    assert test_node1.get_next() == test_node2


def test_get_prev():
    """Test node class get prev method."""
    from double_link import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node2.set_prev(test_node1)
    assert test_node2.get_prev() == test_node1


def test_double_link():
    """Test double_link class constructor."""
    from double_link import Double_Link
    assert isinstance(Double_Link(), Double_Link)


def test_insert():
    """Test double_link class insert method."""
    from double_link import Double_Link
    dll = Double_Link()
    dll.insert(data[0])
    dll.insert(data[1])
    assert dll.head.data == data[1]


def test_append():
    """Test double_link class append method."""
    from double_link import Double_Link
    dll = Double_Link()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.tail.data == data[1]


def test_pop():
    """Test double_link class pop method."""
    from double_link import Double_Link
    dll = Double_Link()
    dll.insert(data[0])
    dll.insert(data[1])
    assert dll.pop().data == data[1]


def test_shift():
    """Test double_link class shift method."""
    from double_link import Double_Link
    dll = Double_Link()
    dll.append(data[0])
    dll.append(data[1])
    assert dll.shift().data == data[1]


def test_remove():
    """Test double_link class remove method."""
    from double_link import Double_Link
    dll = Double_Link()
    dll.insert(data[0])
    dll.insert(data[1])
    dll.insert(data[2])
    dll.remove(data[1])
    assert dll.tail.prev_node.data == data[2]
    assert dll.head.next_node.data == data[0]
