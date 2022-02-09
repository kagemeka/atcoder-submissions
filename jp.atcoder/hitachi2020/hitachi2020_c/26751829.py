# bipartite graph on tree
import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
    m = len(g)
    g = np.vstack((g, g))
    g[m:, :2] = g[m:, 1::-1]
    return g


@nb.njit
def sort_csgraph(n: int, g: np.ndarray) -> typing.Tuple[(np.ndarray, ) * 3]:
    idx = g[:, 0] << 30 | g[:, 1]
    sort_idx = np.argsort(idx, kind='mergesort')
    g = g[sort_idx]
    original_idx = np.arange(len(g))[sort_idx]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    return g, edge_idx, original_idx


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(ab: np.ndarray) -> typing.NoReturn:
    n = len(ab) + 1
    g = csgraph_to_directed(ab)
    g, edge_idx, _ = sort_csgraph(n, g)

    que = [0]
    dist = np.empty(n, np.int64)
    parent = np.full(n, -1, np.int64)
    dist[0] = 0
    for u in que:
        for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
            if v == parent[u]: continue
            parent[v] = u
            dist[v] = dist[u] ^ 1
            que.append(v)
    b = np.bincount(dist)
    if b[0] < b[1]:
        b[0], b[1] = b[1], b[0]
        dist ^= 1
    k, r = divmod(n, 3)
    a, c = k + (r >= 1), k + (r >= 2)

    p = np.full(n, -1, np.int64)
    x = 1
    for i in range(n):
        if x > n: break
        if dist[i] == 1: continue
        p[i] = x
        x += 3
    x = 2
    t = int(b[i] >= c)
    for i in range(n):
        if x > n: break
        if p[i] != -1 or dist[i] != t: continue
        p[i] = x
        x += 3

    x = 3
    for i in range(n):
        if x > n: break
        if p[i] != -1: continue
        p[i] = x
        x += 3
    for x in p:
        print(x)


def main() -> typing.NoReturn:
    n = int(input())
    ab = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2) - 1
    solve(ab)


main()
