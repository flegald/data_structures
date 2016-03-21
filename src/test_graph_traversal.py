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
    (['A>B', 'C>A', 'C>D', 'D>A'], {
        'depth': {
            'A': ['A', 'B'],
            'B': ['B'],
            'C': ['C', 'D', 'A', 'B'],
            'D': ['D', 'A', 'B']
        },
        'breadth': {
            'A': ['A', 'B'],
            'B': ['B'],
            'C': ['C', 'A', 'D', 'B'],
            'D': ['D', 'A', 'B']
        }
    }),
]


@pytest.fixture(params=CASES)
def depth_case(request):
    edges, result_dict = request.param
    graph = Graph()
    for edge in edges:
        node1, node2 = edge.split('>')
        graph.add_edge(node1, node2)
    return graph, result_dict['depth']


@pytest.fixture(params=CASES)
def breadth_case(request):
    edges, result_dict = request.param
    graph = Graph()
    for edge in edges:
        node1, node2 = edge.split('>')
        graph.add_edge(node1, node2)
    return graph, result_dict['breadth']


def test_depth_first(depth_case):
    graph, tests = depth_case
    for start, expected in tests.items():
        assert graph.depth_first_traversal(start) == expected


def test_breadth_first(breadth_case):
    graph, tests = breadth_case
    for start, expected in tests.items():
        assert graph.breadth_first_traversal(start) == expected
