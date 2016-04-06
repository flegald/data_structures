"""Testing the BST......"""
import pytest


@pytest.fixture()
def node_instance1():
    """Create BST instance."""
    from bst import Node
    node = Node()
    node.val = 4
    return node


@pytest.fixture()
def node_instance2():
    """Create BST instance."""
    from bst import Node
    node = Node()
    node.val = 7
    return node


@pytest.fixture()
def bst():
    """Create empty bst."""
    from bst import Bst
    bst = Bst()
    return bst


@pytest.fixture()
def bst_with_stuff():
    """Create BST with stuff in it."""
    from bst import Bst
    bst = Bst()
    for i in range(1, 21):
        bst.insert(i)
    return bst


# Node constructor test

def test_node_constructor():
    """Test that node works."""
    from bst import Node
    new_node = Node(7)
    assert new_node.val == 7


# Left property tests

def test_left_property(node_instance1, node_instance2):
    """Test left property of Node class."""
    node_instance1.left = node_instance2
    assert node_instance1.left == node_instance2


def test_left_setter_parent(node_instance1, node_instance2):
    """Test that parent works in left setter."""
    node_instance1.left = node_instance2
    assert node_instance2.parent == node_instance1


def test_parent_of_parent_is_none(node_instance1, node_instance2):
    """Test what the title says."""
    node_instance1.left = node_instance2
    assert node_instance2.parent.parent is None


# Right property tests

def test_right_property(node_instance1, node_instance2):
    """Test right property of Node class."""
    node_instance1.right = node_instance2
    assert node_instance1.right == node_instance2


def test_right_setter_parent(node_instance1, node_instance2):
    """Test that parent works in right setter."""
    node_instance1.right = node_instance2
    assert node_instance2.parent == node_instance1


# Bst Insert Tests

def test_insert_empty(bst):
    """Test what title says."""
    bst.insert(4)
    assert bst.root is not None


def test_insert_empty_val(bst):
    """Test."""
    bst.insert(4)
    assert bst.root.val == 4


def test_one_node_insert(bst):
    """Test."""
    bst.insert(4)
    bst.insert(2)
    assert bst.root.left.val == 2


def test_one_node_insert_parent(bst):
    """Test."""
    bst.insert(4)
    bst.insert(2)
    assert bst.root.left.parent.val == 4


def test_one_node_insert_greater_than(bst):
    """Test."""
    bst.insert(4)
    bst.insert(5)
    assert bst.root.right.val == 5


def test_insert_duplicate(bst):
    """Test can't insert duplicates."""
    bst.insert(4)
    bst.insert(4)
    assert bst.root.left is None and bst.root.right is None


# Contains method tests

def test_is_it_in_there(bst_with_stuff):
    """Test if what I want is in there."""
    assert bst_with_stuff.contains(4)


def test_it_is_not_in_there(bst_with_stuff):
    """Test if it's not there."""
    assert not bst_with_stuff.contains(90)


def test_not_there_empty(bst):
    """Test contains on empty."""
    assert not bst.contains(4)


# Size method test

def test_size_with_stuff(bst_with_stuff):
    """Test."""
    assert bst_with_stuff.size == 20


def test_size_empty(bst):
    """Test."""
    assert bst.size == 0
