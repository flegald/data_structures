An example of classic data structures.

As a weighted graph, this data structure associates a weight integer or float 
as the third tuple item of any edge along with the two connected nodes.

Abstractly, the weight number may represents distance, probability or some other
numerical relationship between the values at two nodes.

#GRAPH:
  Methods:
  - Graph():  instantiate a Weighted Graph object
  - list_nodes():  Return a list of keys present in the graph.
  - list_edges():  Return a list of edges present in the graph, including the weight of the edge.
  - add_node(key):  Add a new node to the graph.
  - add_edge(key, val, weight):  Add a weighted edge between nodes.  Add any nodes not present as nodes in the graph.
  - del_node(key):  Remove an existing node from graph.  Remove any edges containing this node.
  - del_edge(key, val):  Remove an existing edge from two nodes.
  - has_node(key):  Return True if node exists, False if node not present.
  - neighbors(key):  Return neighbors of a given node.
  - adjacent(key, val):  Returns True if two given nodes are adjacent, False if not.
  - depth_first_traversal(start):  Traverse the graph by depth returning a list in order of path taken.
  - breadth_first_traversal(start):  Traverse the graph by breadth returning a list in order of path taken.
  - dijkstra(start, end):  find the shortest path from start to end using Dijkstra's algorithm.  Dijkstra's algorithm traverses the entire graph detecting the shortest path from start to each node.  From this, a path from end, tracing back to start, is constructed.  Dijkstra's algorithm is effective when total shortest path is desired (accuracy over speed).
  - a_star(start, end):  find the shortest path fromm start to end using a* method.  A* is a modified Dijkstra search adding a heuristic to determine which node to explore next.  The heuristic algorithm will increase speed at the cost of accuracy.  The specific heuristic used will determine the overall loss accuracy and gain of speed (speed over accuracy).

References:
  - Python time complexity (determine which data structures to use for what):  https://wiki.python.org/moin/TimeComplexity
  - Python set data structure:  https://docs.python.org/3/tutorial/datastructures.html#sets
  - Python queue data structure:  https://docs.python.org/3/library/queue.html
  - Wikipedia Dijkstra's algorithm:  https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
  - Wikipedia A* algorithm:  https://en.wikipedia.org/wiki/A*_search_algorithm


#BINARY SEARCH TREE
  (2016/10/4)
  Methods:

    - BST(): Instantiate a Binary Search Tree object.
    - insert(): Add node object to tree.
    - contains(): Checks whether a given value is in the tree.
    - size(): Returns int signifying number of values stored in tree.
    - depth(): Returns int signifying how many levels deep the tree is.
    - balance(): Returns int signifying whether or not the left and right sides of the tree have an even depth.
    - delete(): Remove node from tree.


  Traversals:

  - in_order(): Traverses list in order of left, self, right.
  - pre_order(): Traverses list in order of self, left, right.
  - post_order(): Traverses list in order of left, right, self.
  - breath_first_search(): Traverses list in breath first order.
