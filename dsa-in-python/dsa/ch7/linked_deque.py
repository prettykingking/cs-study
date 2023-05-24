"""Implementing a Deque with Doubly Linked List"""

from dsa.ch7.empty import Empty
from dsa.ch7.doubly_linked import DoublyLinkedBase


class LikedDeque(DoublyLinkedBase):
    """Double-Ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the first element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element      # real item just after header

    def last(self):
        """Return (but do not remove) the last element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element     # real iterm just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)       # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)     # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._trailer._prev)
