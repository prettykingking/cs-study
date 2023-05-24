"""Separate Chaining
"""

from dsa.ch10.hash_map_base import HashMapBase
from dsa.ch10.unsorted_table_map import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))     # no match found
        return bucket[k]                                # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()         # bucket is new to the table
        old_size = len(self._table(j))
        self._table[j][k] = v
        if len(self._table[j]) > old_size:              # key was new to the table
            self._n += 1                                # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))     # no match found
        del bucket[k]                                   # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                      # a non-empty slot
                for key in bucket:
                    yield key
