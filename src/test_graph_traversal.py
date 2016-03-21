"""Test graph_traversal depth-first and breadth-first search functions."""

import pytest
# from string import printable
from graph import Graph

# Every test should return a graph and a simple solution dict.


CASES = [
    (['A>B'], {'A': ['A', 'B'], 'B': ['B']}),
    (['A>B', 'B>A'], {'A': ['A', 'B'], 'B': ['B', 'A']})
]


@pytest.fixture(params=CASES)
def test_case(request):
    edges, result_dict = request.param
    graph = Graph()
    for edge in edges:
        node1, node2 = edge.split('>')
        graph.add_edge(node1, node2)
    return graph, result_dict


def test_graph(test_case):
    graph, tests = test_case
    for start, expected in tests.items():
        assert graph.depth_first_traversal(start) == expected
