"""Singly linked list"""

from dsa.ch7.empty import Empty


class LinkedStack:
    """LIFO Stack implementation using a singly list for storage."""

    class _Node:
        """Lightweight non-public class for singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, e, n):   # initialize node’s fields
            self._element = e       # reference to user’s element
            self._next = n          # reference to next node

    def __init__(self):
        """Create empty stack."""
        self._head = None   # reference to the head node
        self._size = 0      # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack. (e.g. LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
