# _*_  coding:utf-8 _*_
"""Test graph data structure."""
import pytest

NODES = ['A', 'B', 'C', 'D', 'E', 'F']
EDGES = [
    ('A', 'B', 1),
    ('A', 'C', 2),
    ('B', 'D', 4),
    ('B', 'E', 8),
    ('D', 'F', 16),
]


@pytest.fixture(scope='function')
def instance():
    """Create an instance of Graph."""
    from weighted_graph import Graph
    inst = Graph()
    for edge in EDGES:
        inst.add_edge(*edge)
    return inst


@pytest.fixture(scope='function')
def empty_instance():
    """Create an instance of Graph."""
    from weighted_graph import Graph
    return Graph()


def test_graph(instance):
    """Test Graph object."""
    from weighted_graph import Graph
    assert isinstance(instance, Graph)


def test_list_nodes(instance):
    """Test list_nodes method."""
    assert sorted(instance.list_nodes()) == NODES


def test_list_edges(instance):
    """Test list_edges method."""
    assert sorted(instance.list_edges()) == EDGES


def test_add_node(instance):
    """Test add_node method."""
    instance.add_node('G')
    assert sorted(instance.list_nodes()) == NODES + ['G']


def test_add_edge_none_existing(empty_instance):
    """Test add_edge method."""
    new_edge = ('D', 'B', 32)
    empty_instance.add_edge(*new_edge)
    assert sorted(empty_instance.list_edges()) == [new_edge]
    assert sorted(empty_instance.list_nodes()) == ['B', 'D']


def test_add_edge_one_existing(instance):
    """Test add_edge method."""
    new_edge = ('D', 'Q', 32)
    instance.add_edge(*new_edge)
    assert sorted(instance.list_edges()) == sorted(EDGES + [new_edge])
    assert sorted(instance.list_nodes()) == NODES + ['Q']


def test_add_edge_two_existing(instance):
    """Test add_edge method."""
    new_edge = ('D', 'B', 32)
    instance.add_edge(*new_edge)
    assert sorted(instance.list_edges()) == sorted(EDGES + [new_edge])
    assert sorted(instance.list_nodes()) == NODES


def test_del_node(instance):
    """Test del_node method."""
    expected_nodes = list(NODES)
    expected_nodes.remove('E')
    expected_edges = list(EDGES)
    expected_edges.remove(('B', 'E', 8))

    instance.del_node('E')

    assert sorted(instance.list_nodes()) == expected_nodes
    assert sorted(instance.list_edges()) == expected_edges


def test_del_node_empty(empty_instance):
    """Test del_node method."""
    with pytest.raises(KeyError):
        empty_instance.del_node('Z')


def test_del_edge(instance):
    """Test del_edge method."""
    expected_edges = list(EDGES)
    expected_edges.remove(('B', 'E', 8))

    instance.del_edge('B', 'E')
    assert sorted(instance.list_edges()) == expected_edges


def test_has_node_true(instance):
    """Test has_node method."""
    assert instance.has_node('A')


def test_has_node_false(instance):
    """Test has_node method."""
    assert not instance.has_node('Z')


def test_neighbors(instance):
    """Test neighbors method."""
    assert sorted(instance.neighbors('B')) == [('D', 4), ('E', 8)]


def test_adjacent_true(instance):
    """Test adjacent method."""
    assert instance.adjacent('A', 'B')


def test_adjacent_false(instance):
    """Test adjacent method."""
    assert not instance.adjacent('A', 'F')


def test_adjacent_error(instance):
    """Test adjacent method."""
    with pytest.raises(KeyError):
        instance.adjacent('X', 'A')
