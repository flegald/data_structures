# -*- conding: utf-8 -*-
"""TODO: Docstring."""
data = "123"


def test_Node():
    from linked_list import Node
    assert isinstance(Node(data), Node)


def test_set_next():
    from linked_list import Node
    test_node1 = Node(123)
    test_node2 = Node(456)
    test_node1.set_next(test_node2)
    assert test_node1.next_node == test_node2


def test_get_data():
    from linked_list import Node
    test_node = Node(123)
    assert test_node.get_data() == 123


def test_set_data():
    from linked_list import Node
    test_node = Node(123)
    test_node.set_data(456)
    assert test_node.get_data() == 456


def test_get_next():
    from linked_list import Node
    test_node1 = Node(123)
    test_node2 = Node(456)
    test_node1.set_next(test_node2)
    assert test_node1.get_next() == test_node2


def test_Linked_List():
    from linked_list import Linked_List
    assert isinstance(Linked_List(), Linked_List)


def test_insert():
    from linked_list import Linked_List
    from linked_list import Node
    test_list = Linked_List()
    test_insert = test_list.insert(123)
    assert isinstance(test_list.head, Node)


def test_pop():
    from linked_list import Linked_List
    from linked_list import Node
    test_list = Linked_List()
    test_list.insert(123)
    assert isinstance(test_list.pop(), Node)


def test_length():
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(123)
    test_list.insert(456)
    assert test_list.size() == 2


def test_search():
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(123)
    test_list.insert(456)
    assert test_list.search(123) == 123


def test_remove():
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(123)
    test_list.insert(456)
    test_list.insert(789)
    test_list.insert(111)
    test_list.insert(222)
    test_list.remove(456)
    assert test_list.size() == 4


def test_display():
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(123)
    test_list.insert(456)
    assert test_list.display() == "(123, 456)"
