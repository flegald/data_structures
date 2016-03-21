# _*_  coding:utf-8 _*_
"""Test graph data structure."""

DATA = [1, 2, 3, 4]


def test_graph():
    """Test Graph object."""
    from graph import Graph
    graph = Graph()
    assert isinstance(graph, Graph)


def test_list_nodes():
    """Test list_nodes method."""
    from graph import Graph
    graph = Graph()
    graph.g = {'a': [DATA[0], DATA[1]] , 'b': [DATA[1]]}
    assert 'a' in graph.list_nodes()


def test_list_edges():
    """Test list_edges method."""
    from graph import Graph
    graph = Graph()
    graph.g = {'a': [DATA[0], DATA[1]], 'b': [DATA[1]]}
    assert ('a', 1) in graph.list_edges()


def test_add_node():
    """Test add_node method."""
    from graph import Graph
    graph = Graph()
    graph.add_node(DATA[1])
    assert list(graph.g.keys())[0] == DATA[1]


def test_add_edge():
    """Test add_edge method."""
    from graph import Graph
    graph = Graph()
    graph.add_node(DATA[1])
    graph.add_node(DATA[0])
    graph.add_edge(DATA[1], DATA[0])
    assert graph.g[DATA[1]][0] is DATA[0]


def test_add_edge_empty():
    """Test add_edge method."""
    from graph import Graph
    graph = Graph()
    graph.add_edge(DATA[1], DATA[0])
    assert graph.g[DATA[1]][0] is DATA[0]


def test_del_node():
    """Test del_node method."""
    from graph import Graph
    graph = Graph()
    graph.add_node(DATA[1])
    graph.add_node(DATA[0])
    graph.del_node(DATA[1])
    assert DATA[1] not in graph.g.keys()


def test_del_node_empty():
    """Test del_node method."""
    from graph import Graph
    graph = Graph()
    assert graph.del_node(DATA[1]) == "Node does not exist"


def test_del_edge():
    """Test del_edge method."""
    from graph import Graph
    graph = Graph()
    graph.add_edge(DATA[1], DATA[0])
    graph.del_edge(DATA[1], DATA[0])
    assert DATA[0] not in graph.g[DATA[1]]


def test_has_node():
    """Test has_node method."""
    from graph import Graph
    graph = Graph()
    graph.add_node(DATA[1])
    graph.add_node(DATA[0])
    assert graph.has_node(DATA[1]) is True


def test_neighbors():
    """Test neighbors method."""
    from graph import Graph
    graph = Graph()
    graph.add_node(DATA[1])
    graph.add_node(DATA[0])
    graph.add_edge(DATA[1], DATA[0])
    assert graph.neighbors(DATA[1]) == [DATA[0]]


def test_adjacent():
    """Test adjacent method."""
    from graph import Graph
    graph = Graph()
    graph.add_node(DATA[1])
    graph.add_node(DATA[0])
    graph.add_edge(DATA[1], DATA[0])
    assert graph.adjacent(DATA[1], DATA[0]) is True 

