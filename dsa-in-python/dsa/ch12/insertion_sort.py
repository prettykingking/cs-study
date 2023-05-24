"""Insertion sort
"""

def insertion_sort(seq):
    for k in range(1, len(seq)):
        cur = seq[k]
        j = k
        while j > 0 and seq[j - 1] > cur:
            seq[j] = seq[j - 1]
            j -= 1
        seq[j] = cur
    return seq
