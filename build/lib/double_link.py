#  _*_ coding: utf-8 _*__
"""Implement a double linked list data structure."""


class Node(object):
	"""Create Node object."""

	def __init__(self, data=None, next_node=None, prev_node=None):
		"""Instantiate Node object."""
		self.data = data
		self.next_node = next_node
		self.prev_node = prev_node

	def set_next(self, next):
		"""change node that self is pointing to."""
		self.next_node = next_node

	def get_data(self):
		"""Access self Node's data."""
		return self.data

	def get_next(self):
		"""Access Node self Node is pointing to."""
		return self.next_node

	def set_data(self, data):
		"""Insert data into self Node."""
		self.data = data

	def get_prev(self):
		"""Access Node that self Node is pointing back to."""
		return self.prev_node

	def set_prev(self, prev):
		"""Set Node that self Node points back to."""
		self.prev_node = prev

	class Double_Link(object):
		"""Create Double List Object"""

		def __init__(self, head=None, tail=None):
			"""Instantiate double link."""
			self.head = head
			self.tail = tail

		def insert(self, data):
			"""Insert Node into head of list"""
			self.head = Node(data, self.head)

		def append(self, data):
			"""Insert Node into tail of list."""
			self.tail = Node(data, None, self.tail)

		def pop(self):
			"""Remove and return head of list."""
			head = self.head
			self.head = head.next_node
			return head

		def shift(self):
			"""Remove and return tail of list."""
			tail = self.tail
			self.tail = tail.prev_node
			return tail

		def remove(self, data):
			"""Remove a specific Node from the list."""
			node = self.head
			while True:
				if node.data == data:
					try:
						node.next_node.prev_node = node.prev_node
					except: 
						self.tail = node.prev_node

					try:
						node.prev_node.next_node = node.next_node
					except:
						self.head = node.next_node
					break

				else:
					 node = node.next_node






