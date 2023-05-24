"""Tests for chapter 10
"""

from dsa.ch10.sorted_table_map import SortedTableMap


def test_sorted_table_map():
    tm = SortedTableMap()
    tm[3] = 'c'
    tm[1] = 'a'
    tm[2] = 'b'
    min_k, min_v = tm.find_min()
    assert min_k == 1
    max_k, max_v = tm.find_max()
    assert max_k == 3
