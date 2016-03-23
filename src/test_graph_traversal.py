"""Test graph_traversal depth-first and breadth-first search functions."""

import pytest
# from string import printable
from graph import Graph

# Every test should return a graph and a simple solution dict.


CASES = [
    (['A>B'], {
        'depth': {
            'A': ['A', 'B'],
            'B': ['B']
        },
        'breadth': {
            'A': ['A', 'B'],
            'B': ['B']
        }
    }),
    (['B>A', 'A>B'], {
        'depth': {
            'B': ['B', 'A'],
            'A': ['A', 'B'],
        },
        'breadth': {
            'B': ['B', 'A'],
            'A': ['A', 'B'],
        }
    }),
    (['A>B', 'B>C', 'C>A'], {
        'depth': {
            'A': ['A', 'B', 'C'],
            'B': ['B', 'C', 'A'],
            'C': ['C', 'A', 'B']
        },
        'breadth': {
            'A': ['A', 'B', 'C'],
            'B': ['B', 'C', 'A'],
            'C': ['C', 'A', 'B']
        }
    }),
    (['A>B', 'C>A', 'C>D', 'D>A'], {
        'depth': {
            'A': ['A', 'B'],
            'B': ['B'],
            'C': ['C', 'A', 'B', 'D'],
            'D': ['D', 'A', 'B']
        },
        'breadth': {
            'A': ['A', 'B'],
            'B': ['B'],
            'C': ['C', 'A', 'D', 'B'],
            'D': ['D', 'A', 'B']
        }
    }),
    (['A>B', 'A>E', 'B>C', 'B>D', 'E>F', 'E>G'], {
        'depth': {
            'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'B': ['B', 'C', 'D'],
            'E': ['E', 'F', 'G']
        },
        'breadth': {
            'A': ['A', 'B', 'E', 'C', 'D', 'F', 'G'],
            'B': ['B', 'C', 'D'],
            'E': ['E', 'F', 'G']
        }
    }),
]


@pytest.fixture(params=CASES)
def depth_case(request):
    """Assemble a Graph and returned the expected result for a depth search."""
    edges, result_dict = request.param
    graph = Graph()
    for edge in edges:
        node1, node2 = edge.split('>')
        graph.add_edge(node1, node2)
    return graph, result_dict['depth']


@pytest.fixture(params=CASES)
def breadth_case(request):
    """Return a Graph and expected results for a breadth search."""
    edges, result_dict = request.param
    graph = Graph()
    for edge in edges:
        node1, node2 = edge.split('>')
        graph.add_edge(node1, node2)
    return graph, result_dict['breadth']


def test_depth_first(depth_case):
    """Test that depth first search returns the expected search path."""
    graph, tests = depth_case
    for start, expected in tests.items():
        assert graph.depth_first_traversal(start) == expected


def test_breadth_first(breadth_case):
    """Test that breadth first search returns the expected search path."""
    graph, tests = breadth_case
    for start, expected in tests.items():
        assert graph.breadth_first_traversal(start) == expected
