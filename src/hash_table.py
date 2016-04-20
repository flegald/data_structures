"""Hash table implementation."""




class HashTable(object):
    """Hash Table."""

    def __init__(self):
        """Initialize hash table."""
        self._size = 1024
        self._table = [None] * self._size

    def get(self, key):
        """Look item up in table."""
        if not isinstance(key, str):
            raise TypeError(key, type(key), "Key must be a string!")

        hashed = self._hashing(key, self._size)

        if self._table[hashed]:
            for i in self._table[hashed]:
                if i[0] == hashed:
                    return i[1]

        raise KeyError(key)

    def set(self, key, val):
        """Insert into table."""
        hashed = self._hashing(key, self._size)
        if self._table[hashed]:
            self._table[hashed].append((hashed, val))
        else:
            self._table[hashed] = [(hashed, val)]

    def 

    def _hashing(self, string, table_size):
        """Hash function."""
        summed = 0
        for i in range(len(string)):
            summed = summed + ord(string[i])
        return summed % table_size
