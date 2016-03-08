# -*- conding: utf-8 -*-
"""Doctstring."""

class Node(object):
    """Doctstring."""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


    def set_next(self, next):
        self.next_node = next


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next_node


    def set_data(self, data):
        self.data = data


class Linked_List(object):
    def __init__(self, head=None, length=0):
        self.head = head
        self.length = length


    def insert(self, data):
        self.length += 1    
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node


    def pop(self):
        old_head = self.head
        self.head = old_head.get_next()
        return old_head

    def size(self):
        return self.length

    def search(self, data):
        node = self.head
        for i in range(self.size()):
            if node.get_data() == data:
                return node.get_data()
            else:
                node = node.get_next()

    def remove(self, data):
        node = self.head
        node_prev = None
        for i in range(self.size()):
            if node.get_data() == data:
                if node_prev:
                    node_prev.set_next(node)
                    self.length = self.length - 1

                else:
                   self.pop()
                break
            else:
                node_prev = node
                node = node.get_next()

    def display(self):
        add_to = ")"
        node = self.head
        for i in range(self.size()):
            add_to = str(node.get_data()) + add_to
            if node.get_next():
                add_to = ', ' + add_to
            node = node.get_next()
        add_to = '(' + add_to
        return add_to
            


