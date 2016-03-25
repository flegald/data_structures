#  _*_ coding: utf-8 _*_
"""Create a graph type data structure."""
import time
import random
from math import inf
from collections import deque
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

    def _list_edges(self):
        """Create list of edges in graph."""
        keys = self.g.keys()
        edge_list = []
        for key in keys:
            zipper = zip_longest(key, self.g[key].items(), fillvalue=key)
            while True:
                try:
                    edge_list.append(next(zipper))
                except StopIteration:
                    break
        return edge_list

    def list_edges(self):
        """Create list of edges in graph."""
        return [(key, val, weight)
                for key, inner_dict in self.g.items()
                for val, weight in inner_dict.items()]

    def add_node(self, key):
        """Add node to graph."""
        self.g.setdefault(key, {})

    def add_edge(self, key, val, weight):
        """Add edge between nodes."""
        self.g.setdefault(key, {})[val] = weight
        self.g.setdefault(val, {})

    def del_node(self, key):
        """Remove node from graph."""
        try:
            del self.g[key]
            for k, inner_dict in self.g.items():
                inner_dict.pop(key, None)
        except (KeyError, IndexError):
            raise KeyError("Node does not exist.")

    def del_edge(self, key, val):
        """Remove edge from nodes."""
        try:
            del self.g[key][val]
        except KeyError:
            raise KeyError("Edge does not exist.")

    def has_node(self, key):
        """Return a boolean whether node exists."""
        return key in self.g

    def neighbors(self, key):
        """Return neighbors."""
        try:
            return list(self.g[key].items())
        except KeyError:
            raise KeyError("Node not present")

    def adjacent(self, key, val):
        """See is nodes are adjacent."""
        try:
            return val in self.g[key]
        except KeyError:
            raise KeyError("{} is not a node in this graph.".format(key))

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
        queue = deque(start)
        visited = set()
        path = []
        while bool(len(queue)):
            cursor = queue.popleft()
            if cursor not in visited:
                visited.add(cursor)
                for item in self.g[cursor]:
                    queue.append(item)
                path.append(cursor)
        return path

    def dijkstra(self, start, end):
        """Dijkstra shortest path algorithm."""
        current = start
        unvisited = set([start])
        visited = set()
        distances = {key: (inf, None) for key in self.g}
        distances[current] = (0, None)
        while unvisited:
            shortest_tent_dist = inf
            next_current = None
            for neighbor, distance in self.g[current].items():
                tent_dist = distances[current][0] + distance
                if neighbor not in visited:
                    unvisited.add(neighbor)
                    if tent_dist < shortest_tent_dist:
                        next_current = neighbor
                        shortest_tent_dist = tent_dist
                if tent_dist < distances[neighbor][0]:
                    distances[neighbor] = (tent_dist, current)
            unvisited.discard(current)
            visited.add(current)
            try:
                current = next_current or unvisited.pop()
            except KeyError:
                break
        path_rev = []
        best_prev = end
        while best_prev is not None:
            path_rev.append(best_prev)
            best_prev = distances[best_prev][1]
            # import pdb; pdb.set_trace()
        return reversed(path_rev)

    def a_star(self, start, end):
        """A* heuristic shortest path algorithm."""
        current = start
        unvisited = set([start])
        visited = set()
        distances = {key: (inf, None) for key in self.g}
        heur_distances = {key: (inf, None) for key in self.g}
        distances[current] = (0, None)
        heur_distances[current] = self._heuristic(current)
        while unvisited:

            for neighbor, distance in self.g[current].items():
                tent_dist = distances[current][0] + distance
                if neighbor not in visited:
                    unvisited.add(neighbor)
                if tent_dist < distances[neighbor][0]:
                    distances[neighbor] = (tent_dist, current)
            unvisited.discard(current)
            visited.add(current)

            # Use a heuristic function to calculate the best next move.
            try:
                current = self._heuristic(current) or unvisited.pop()
            except KeyError:
                break

        path_rev = []
        best_prev = end
        while best_prev is not None:
            path_rev.append(best_prev)
            best_prev = distances[best_prev][1]
        return reversed(path_rev)

    def _heuristic(self, current):
        """Estimate next best move considering connected nodes' weight edge."""
        next_values = {}
        for conn in self.g[current]:
            next_weights = sum([weight for weight in self.g[conn].values()])
            next_values[conn] = next_weights
        if not next_values:
            return None
        return min(next_values, key=lambda k: next_values[k])


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
