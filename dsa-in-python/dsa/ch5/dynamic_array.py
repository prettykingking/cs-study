"""Dynamic array
"""

import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        """Return elements at index k"""
        if 0 <= k < self._n:
            return self._array[k]                   # retrieve from array
        else:
            raise IndexError('invalid index')

    @staticmethod
    def make_array(c):
        """Returns new array with capacity c."""
        return (c * ctypes.py_object)()             # create array with fixed number of elements

    def append(self, item):
        """Add object to the end of the array"""
        if self._n == self._capacity:               # not enough room
            self._resize(self._capacity * 2)        # so double capacity
        self._array[self._n] = item
        self._n += 1

    def _resize(self, c):
        n_array = self.make_array(c)               # new (bigger) array
        for k in range(self._n):                    # for each existing value
            n_array[k] = self._array[k]
        self._array = n_array                       # use the bigger array
        self._capacity = c
