"""Tests for chapter 9"""

from dsa.ch9.sorted_priority_queue import SortedPriorityQueue
from dsa.ch9.unsorted_priority_queue import UnsortedPriorityQueue


def test_sorted_priority_queue():
    pq = SortedPriorityQueue()
    pq.add(3, 'c')
    min_tuple = pq.min()
    assert min_tuple[0] == 3
    assert len(pq) == 1
    pq.add(1, 'a')
    min_tuple = pq.min()
    assert min_tuple[0] == 1
    assert len(pq) == 2

def test_unsorted_priority_queue():
    pq = UnsortedPriorityQueue()
    pq.add(4, 'd')
    min_tuple = pq.min()
    assert min_tuple[0] == 4
    assert len(pq) == 1
    pq.add(2, 'b')
    min_tuple = pq.min()
    assert min_tuple[0] == 2
    assert len(pq) == 2
