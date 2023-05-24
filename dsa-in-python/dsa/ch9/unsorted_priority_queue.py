"""Implementation with an Unsorted List"""

from dsa.ch7.empty import Empty
from dsa.ch7.positional_list import PositionalList
from dsa.ch9.priority_queue import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):
    """A mini-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """Create an new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the Priority Queue."""
        return len(self._data)

    def _find_min(self):
        """Return position of item with minimum key."""
        if self.is_empty():
            raise Empty('priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
