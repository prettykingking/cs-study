"""Priority Queues"""


class PriorityQueueBase:
    """Abstract class for a priority queue."""

    class _Item:
        """lightweight composite to store priority store items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

    def __len__(self):
        """Return the total number of elements in the priority queue."""
        raise NotImplementedError('must be implemented by subclass')

    def is_empty(self):         # concrete method assuming abstract len
        """Returns True if the priority queue is empty."""
        return len(self) == 0
