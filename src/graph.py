#  _*_ coding: utf-8 _*_
"""Create a graph type data structure."""
from queue import Queue
try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest


class Graph(object):
    """Graph data structure."""

    def __init__(self):
        """Instantiate Graph."""
        self.g = {}

    def list_nodes(self):
        """Create a list of keys in graph."""
        return self.g.keys()

    def list_edges(self):
        """Create list of edges in graph."""
        keys = self.g.keys()
        edge_list = []
        for key in keys:
            zipper = zip_longest(key, self.g[key], fillvalue=key)
            while True:
                try:
                    edge_list.append(next(zipper))
                except StopIteration:
                    break
        return edge_list

    def add_node(self, key):
        """Add node to graph."""
        self.g.setdefault(key, [])

    def add_edge(self, key, val):
        """Add edge between nodes."""
        self.g.setdefault(key, []).append(val)
        self.g.setdefault(val, [])

    def del_node(self, key):
        """Remove node from graph."""
        try:
            self.g.pop(key)
        except (KeyError, IndexError):
            return "Node does not exist"

    def del_edge(self, key, val):
        """Remove edge from nodes."""
        self.g[key].pop(self.g[key].index(val))

    def has_node(self, key):
        """Return a boolean whether node exists."""
        return key in list(self.g.keys())

    def neighbors(self, key):
        """Return neighbors."""
        try:
            return self.g[key]
        except KeyError:
            return "Node not present"

    def adjacent(self, key, val):
        """See is nodes are adjacent."""
        try:
            return val in self.g[key]
        except KeyError:
            return "Node does not exist"

    def depth_first_traversal(self, start):
        """Traverse the graph by depth."""
        stack = [start]
        visited = set()
        path = []
        while stack:
            cursor = stack.pop()
            if cursor not in visited:
                stack.extend(self.g[cursor])
                visited.add(cursor)
                path.append(cursor)
        return path

    def breadth_first_traversal(self, start):
        """Traverse the graph by breadth."""
        queue = Queue()
        queue.put(start)
        visited = set()
        path = []
        while queue:
            cursor = queue.get()
            if cursor not in visited:
                visited.add(cursor)
                queue.add(self.g[cursor])
                path.append(cursor)
        return path


