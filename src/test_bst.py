"""Testing the BST......"""
import pytest


@pytest.fixture()
def empty_node():
    """Create empty node instance."""
    from bst import Node
    node = Node()
    return node


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


# Bst insert tests

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


# Size method tests

def test_size_with_stuff(bst_with_stuff):
    """Test."""
    assert bst_with_stuff.size == 20


def test_size_empty(bst):
    """Test."""
    assert bst.size == 0


# Depth method tests

def test_depth_empty(empty_node):
    """Test one empty node has no depth."""
    assert empty_node.depth() == 0


def test_one_node_depth(node_instance1):
    """Test one node with val has deoth."""
    assert node_instance1.depth() == 1


def test_bst_depth_larger(bst):
    """Test depth of bst with many nodes."""
    bst.insert(4)
    bst.insert(5)
    bst.insert(7)
    assert bst.depth() == 3


def test_bst_depth_smaller(bst):
    """Test depth of bst with many nodes."""
    bst.insert(4)
    bst.insert(5)
    bst.insert(3)
    assert bst.depth() == 2


# Test Balance

def test_empty_balance(bst):
    """Test balance on empty tree."""
    assert not bst.balance()


def test_single_node_balance(bst):
    """Test single node bst balance."""
    bst.insert(1)
    assert bst.balance() == 0


def test_bst_multiple_nodes_balance(bst):
    """Test two node balance."""
    bst.insert(4)
    bst.insert(3)
    assert bst.balance() == 1


def test_for_negative_balance(bst):
    """Test fior negative balance result."""
    bst.insert(4)
    bst.insert(5)
    assert bst.balance() == -1


def test_more_nodes(bst):
    """More balance test."""
    bst.insert(4)
    bst.insert(5)
    bst.insert(2)
    bst.insert(1)
    assert bst.balance() == 1


# In order traversal tets

def test_empty_in_order(bst):
    """Test empty in_order."""
    assert not list(bst.in_order())


def test_in_order_with_stuff(bst):
    """Test in-order on multiple nodes."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert list(bst.in_order()) == [1, 2, 3, 4]


# Pre order traversal tests

def test_pre_order_empty(bst):
    """Test pre-order empty."""
    assert not list(bst.pre_order())


def test_pre_order_with_stuff(bst):
    """Test pre-order on multiple nodes."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert list(bst.pre_order()) == [4, 2, 1, 3]

# Post ordered traversal


def test_post_order_empty(bst):
    """Test post-order empty."""
    assert not list(bst.pre_order())


def test_post_order_with_stuff(bst):
    """Test post-order on multiple nodes."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert list(bst.post_order()) == [1, 3, 2, 4]


# Breadth first traversal

def test_empty_breadth(bst):
    """Test empty breadth first."""
    assert list(bst.breadth_first()) == []


def test_breadth_with_stuff(bst):
    """Test breadth with stuff."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    assert list(bst.breadth_first()) == [4, 2, 5, 1, 3]

# Delete method


def test_delete_empty(bst):
    """Test empty delete."""
    assert not bst.delete(1)


def test_return_none_with_stuff(bst_with_stuff):
    """Test return None when val not found."""
    assert not bst_with_stuff.delete(9000)


