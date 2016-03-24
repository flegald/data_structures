"""Test algorthims for finding the shortest path in a weighted graph."""

import pytest

# Make this more complex
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


@pytest.mark.parametrize("origin, destination, distance", GEO_EDGES)
def test_sea_port(geo_instance, origin, destination, distance):
    assert list(geo_instance.dijkstra(origin, destination)) == [origin, destination]

def test_isoloated_node(geo_instance):
    assert list(geo_instance.dijkstra('Dallas', 'Dallas')) == ['Dallas']


def test_1(geo_instance):
    assert list(geo_instance.dijkstra('Seattle', 'Los Angeles')) == ['Seattle', 'San Francisco', 'Los Angeles']


def test_2(geo_instance):
    assert list(geo_instance.dijkstra('Salt Lake City', 'San Francisco')) == ['Salt Lake City', 'Portland', 'San Francisco']


def test3(another_instance):
    assert list(another_instance.dijkstra('A', 'B')) == ['A', 'D', 'E', 'B']
