"""Tests for chapter 11
"""

from dsa.ch11.tree_map import TreeMap


def test_tree_map():
    tree_map = TreeMap()
    tree_map[142] = 142
    tree_map[86] = 86
    tree_map[157] = 157
    tree_map[77] = 77
    tree_map[96] = 96
    tree_map[143] = 143
    tree_map[168] = 168
    tree_map[66] = 66
    tree_map[80] = 80
    tree_map[88] = 88
    tree_map[98] = 98
    tree_map[160] = 160
    tree_map[178] = 178

    assert tree_map.is_empty() == False
    assert tree_map.height(tree_map.root()) == 3
    assert tree_map.height(tree_map.find_position(143)) == 0
    assert tree_map.height(tree_map.find_position(168)) == 1
    assert tree_map.first().value() == 66
    assert tree_map.last().value() == 178
