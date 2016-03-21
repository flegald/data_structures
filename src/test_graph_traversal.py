"""Test graph_traversal depth-first and breadth-first search functions."""

import pytest
from string import printable
from graph import Graph

# Every test should return a graph and a simple solution dict.


@pytest.fixture()
def simple_graph():
    """Return graph and a solution dict."""
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    return graph, {'A': ['A', 'B'], 'B': ['B']}


# @pytest.fixture()
# def random_graph():
#     graph = Graph()
#     node_names = list(printable)
#     random.shuffle(node_names)
#     size = random.choice(range(1, len(node_names)))
#     expected = []
#     for n in range(size):
#         name = node_names.pop()

#     return graph


def test_simple(simple_graph):
    graph, tests = simple_graph
    for start, expected in tests.items():
        assert graph.depth_first_traversal(start) == expected
