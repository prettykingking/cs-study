"""Directed graph algorithms
"""

from copy import deepcopy

from dsa.ch14.graph import Graph


def floyd_warshall(g: Graph):
    """Return a new graph that is transitive closure of g."""
    closure = deepcopy(g)               # import from copy package
    verts = list(closure.vertices())    # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge(i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge(k,j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i,j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure


def topological_sort(g: Graph):
    """Return a list of vertices of directed graph g in topological order.

    If graph has a cycle, the result will be incomplete.
    """
    topo = []       # a list of vertices placed in topological  order
    ready = []      # list of vertices that have no remaining constraints
    incount = {}    # keep track of in-degree for each index
    for u in g.vertices():
        incount[u] = g.degree(u, False)     # parameter requests incoming edges
        if incount[u] == 0:                         # if u has no incoming edges
            ready.append(u)                         # it is free of constraints
    while len(ready) > 0:
        u = ready.pop()                 # u is free of constraints
        topo.append(u)                  # add u to the topological order
        for e in g.incident_edges(u):   # consider all outgoing neighbors of u
            v = e.opposite(u)
            incount[v] -= 1             # v has one less than constraint without u
            if incount[v] == 0:
                ready.append(v)
    return topo
