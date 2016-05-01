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

    def traversal(self, word='', start=None):
        """Generator that yields all the words in the Trie."""
        if not word:
            start = self._data
        elif not start:
            start = self._data
            for letter in word:
                try:
                    start = start[letter]
                except KeyError:
                    raise KeyError('Value Does not exist in trie')

        for key in start:
            if key == '$':
                yield word
            else:
                for item in self.traversal(word + key, start[key]):
                    yield item

    def autocomplete(self, start):
        """Return list of top four words completing start input."""
        results = []
        for idx in range(len(start)):
            try:
                results.append(
                    list(sorted(self.traversal(start[:idx + 1])))[:4])
            except ValueError:
                results.append([])
        return results[-1]

    __contains__ = contains
