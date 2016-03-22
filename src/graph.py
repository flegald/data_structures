#  _*_ coding: utf-8 _*_
"""Create a graph type data structure."""
import time
import random
try:
    from itertools import izip_longest as zip_longest
    from Queue import Queue
except ImportError:
    from itertools import zip_longest
    from queue import Queue


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
                stack.extend(self.g[cursor][::-1])
                visited.add(cursor)
                path.append(cursor)
        return path

    def breadth_first_traversal(self, start):
        """Traverse the graph by breadth."""
        queue = Queue()
        queue.put(start)
        visited = set()
        path = []
        while not queue.empty():
            cursor = queue.get()
            if cursor not in visited:
                visited.add(cursor)
                for item in self.g[cursor]:
                    queue.put(item)
                path.append(cursor)
        return path


if __name__ == "__main__":
    # Establish a list of the two methods.
    methods = [Graph.depth_first_traversal, Graph.breadth_first_traversal]
    time_results = {method.__name__: [] for method in methods}

    # Do 40 total trials.
    for n in range(40):
        # Initialize graph instance and create 100 random nodes and edges.
        graph = Graph()
        for i in range(100):
            graph.add_node(random.randrange(1, 101))
        for i in range(100):
            graph.add_edge(random.choice(list(graph.g.keys())),
                           random.choice(list(graph.g.keys())))

        for method in methods:
            # Make a starting point time stamp.
            start_time = time.time()
            # Choose a random start node.
            start_node = random.choice(list(graph.g.keys()))
            # Do a thousand searches on given graph.
            for n in range(1000):
                method(graph, start_node)
            # Check how much time has elapsed since starting time stamp.
            time_delta = time.time() - start_time
            print('{} completed in {} seconds.'.format(
                method.__name__, time_delta))
            # Log the elapsed time for 1000 searches in our time results.
            time_results[method.__name__].append(time_delta)

    # Find the average time of 40000 trials.
    for method_name, times in time_results.items():
        print('{} averaged {} seconds.'.format(
            method_name, sum(times) / float(len(times))))
