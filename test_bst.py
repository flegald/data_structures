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

