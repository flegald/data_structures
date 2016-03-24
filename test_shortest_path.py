"""Test algorthims for finding the shortest path in a weighted graph."""

import pytest

# Make this more complex
EDGES = [
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


@pytest.fixture(scope='function')
def instance():
    """Create an instance of Graph."""
    from weighted_graph import Graph
    inst = Graph()
    for edge in EDGES:
        inst.add_edge(*edge)
    return inst
