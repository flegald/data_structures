"""Test algorthims for finding the shortest path in a weighted graph."""

import pytest

GEO_EDGES = [
    ('Seattle', 'Portland', 145),
    ('Seattle', 'San Francisco', 680),
    ('San Francisco', 'Los Angeles', 348),
    ('Portland', 'San Francisco', 536),
    ('Las Vegas', 'Los Angeles', 229),
    ('Las Vegas', 'Salt Lake City', 363),
    ('Salt Lake City', 'Seattle', 701),
    ('Salt Lake City', 'Portland', 635),
    ('San Francisco', 'Salt Lake City', 600),
]


MORE_EDGES = [
    ('A', 'B', 500),
    ('A', 'C', 3),
    ('A', 'D', 1),
    ('D', 'E', 1),
    ('C', 'B', 3),
    ('E', 'B', 1)
]


@pytest.fixture(scope='function')
def geo_instance():
    """Create an instance of Graph."""
    from weighted_graph import Graph
    inst = Graph()
    for edge in GEO_EDGES:
        inst.add_edge(*edge)
    inst.add_node('Dallas')
    return inst


@pytest.fixture(scope='function')
def another_instance():
    """Create an instance of Graph."""
    from weighted_graph import Graph
    inst = Graph()
    for edge in MORE_EDGES:
        inst.add_edge(*edge)
    return inst


@pytest.fixture(scope='function', params=['dijkstra', 'a_star'])
def method(request, geo_instance):
    """Establish which method we are using for a test."""
    return getattr(geo_instance, request.param)


@pytest.mark.parametrize("origin, destination, distance", GEO_EDGES)
def test_direct_route(method, origin, destination, distance):
    """Test that geographical direct path is the shortest."""
    assert list(method(origin, destination)) == [origin, destination]


def test_isoloated_node(method):
    """Test that a single unconnected node returns only iteself in a path."""
    assert list(method('Dallas', 'Dallas')) == ['Dallas']


def test_1(method):
    """Check a specific expected distance."""
    expected = ['Seattle', 'San Francisco', 'Los Angeles']
    assert list(method('Seattle', 'Los Angeles')) == expected


def test_2(method):
    """Check a specific expected distance."""
    expected = ['Salt Lake City', 'Portland', 'San Francisco']
    assert list(method('Salt Lake City', 'San Francisco')) == expected


def test3(another_instance):
    """Check that shortest route is not most direct on this graph."""
    assert list(another_instance.dijkstra('A', 'B')) == ['A', 'D', 'E', 'B']
