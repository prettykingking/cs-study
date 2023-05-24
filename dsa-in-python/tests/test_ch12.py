"""Tests for chapter 12."""

from dsa.ch12.insertion_sort import insertion_sort


def test_insertion_sort():
    seq = [9, 2, 3, 5, 0, 1, 4, 8, 7, 6]
    sorted_seq = insertion_sort(seq)
    assert sorted_seq[0] == 0
    assert sorted_seq[1] == 1
    assert sorted_seq[2] == 2
    assert sorted_seq[3] == 3
    assert sorted_seq[4] == 4
