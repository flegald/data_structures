An example of classic data structures.

As a weighted graph, this data structure associated a weight integer as the third tuple item of any
edge along with the two connected nodes.

#GRAPH:
(2016/21/03):
  Methods:
  - Graph():  instantiate a Weighted Graph object
  - list_nodes():  Return a list of keys present in the graph.
  - list_edges():  Return a list of edges present in the graph, including the weight of the edge.
  - add_node(key):  Add a new node to the graph.
  - add_edge(key, val):  Add a weighted edge between nodes.  Add any nodes not present as nodes in the graph.
  - del_node(key):  Remove an existing node from graph.  Remove any edges containing this node.
  - del_edge(key, val):  Remove an existing edge from two nodes.
  - has_node(key):  Return True if node exists, False if node not present.
  - neighbors(key):  Return neighbors of a given node.
  - adjacent(key, val):  Returns True if two given nodes are adjacent, False if not.
  - depth_first_traversal(start):  Traverse the graph by depth returning a list in order of path taken.
  - breadth_first_traversal(start):  Traverse the graph by breadth returning a list in order of path taken.

References:
  - Python time complexity (determine which data structures to use for what):  https://wiki.python.org/moin/TimeComplexity
  - Python set data structure:  https://docs.python.org/3/tutorial/datastructures.html#sets
  - Python queue data structure:  https://docs.python.org/3/library/queue.html


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
