"""Brute-Force pattern matching
"""


def brute_force(T: str, P: str):
    """Return the lowest index of T at which subtring P begins (or else -1)."""
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


def find_boyer_moore(T: str, P: str):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    n, m = len(T), len(P)           # introduce convenient notations
    if m == 0: return 0             # trivial search for empty string
    last = {}                       # build 'last' dict
    for k in range(m):
        last[P[k]] = k              # later occurrence overwrites
    # align end of pattern at index m - 1 of text
    i = m - 1                       # an index into T
    k = m - 1                       # an index into P
    while i < n:
        if T[i] == P[k]:            # a matching character
            if k == 0:
                return i            # pattern begins at index i of T
            else:
                i -= 1              # examine previous character
                k -= 1              # of both T and P
        else:
            j = last.get(T[i], -1)  # last (T[i]) is -1 if not found
            i += m - min(k, j + 1)  # case analysis for jump step
            k = m - 1               # restart at end of pattern
    return -1


def find_kmp(T: str, P: str):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    n, m = len(T), len(P)           # introduce convenient notations
    if m == 0: return 0             # trivial search for empty string
    fail = compute_kmp_fail(P)      # rely on utility to precompute
    j = 0                           # index into T
    k = 0                           # index into P
    while j < n:
        if T[j] == P[k]:            # P[0:1+k] matched thus far
            if k == m - 1:          # match is complete
                return j - m + 1
            j += 1                  # try to extend
            k += 1
        elif k > 0:
            k = fail[k - 1]         # reuse suffix of P[0:k]
        else:
            j += 1
    return -1                       # reached end without match


def compute_kmp_fail(P: str):
    """Utility that computes and returns KMP 'fail' list"""
    m = len(P)
    fail = [0] * m              # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:        # compute f(j) during this pass, if nonzero
            fail[j] = k + 1     # k + 1 characters match thus far
            j += 1
            k += 1
        elif k > 0:             # k follows a matching prefix
            k = fail[k - 1]
        else:                   # no match found starting at j
            j += 1
    return fail
