"""Trie class implementation."""
import re

class Trie(object):
    """Trie implementation."""

    def __init__(self):
        """Initialize trie."""

        self._data = {}

    def insert(self, token):
        """Insert token into Trie."""
        acceptable_chars = re.compile(r'[^a-z\']')
        if re.search(acceptable_chars, token) or isinstance(token, int):
            raise TypeError("Token can only contain letters or apostrophies")
        x = self._data
        token += '$'
        for char in token:
            x = x.setdefault(char, {})

    def contains(self, token):
        """Return if token is in Trie."""
        x = self._data
        for char in token:
            try:
                x = x[char]
            except KeyError:
                return False
        return '$' in x

    word = ''
    edge = self._data
    count = 0

    def depth_first(self, start):
        """Traversal."""
        for key in edge:
            if start[count] == edge.keys():
                if key == '$':
                    yield word
                else:
                    word += key
                    self.depth_first(edge[key])
        count += 1

    __contains__ = contains
