"""Implementation of Linked Binary Tree Structure"""

from dsa.ch8.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:
        """Lightweight, non-public class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An Abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container: LinkedBinaryTree = container
            self._node: LinkedBinaryTree._Node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same Position."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p: Position):
        """Return associated node, if Position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p must not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')        # convention for deprecated nodes
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # ---------- binary tree constructor ----------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # ---------- public accessors ----------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p: Position):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p: Position):
        """Return the Position of p's left child (or None if p has no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p: Position):
        """Return the Position of p's right child (or None if p has no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p: Position):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:      # left child exists
            count += 1
        if node._right is not None:     # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """Place an element at the root of an empty tree and return new Position.

        Raise ValueError if tree non-empty.
        """
        if self._root is not None:
            raise ValueError('root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create new left child for Position p, storing element e.

        Return the Position of e.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create new right child of Position p, storing element e.

        Return the Position of e.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at Position p with e, and return old element.
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with it's child, if any.

        Return the element that stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        if node._left:
            child = node._left
        else:
            child = node._right
        if child is not None:
            child._parent = node._parent    # child's grandparent becomes parent
        if node is self._root:
            self._root = child              # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -=1
        node._parent = node                 # convention for deprecated node
        return node._element

    def _attach(self, p, tl, tr):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(tl) is type(tr):          # all 3 trees must be the same type
            raise ValueError('tree types must be match')
        self._size += len(tl) + len(tr)
        if not tl.is_empty():           # attach tl as left subtree of node
            tl._root._parent = node
            node._left = tl._root
            tl._root = None             # set tl instance to empty
            tl._size = 0
        if not tr.is_empty():           # attach tr as right subtree of node
            tr._root._parent = node
            node._right = tr._root
            tr._root = None             # set tr instance to empty
            tr._size = 0
