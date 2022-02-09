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



@nb.njit
def compress_array(a: np.ndarray) -> typing.Tuple[(np.ndarray, ) * 2]:
    v = np.unique(a)
    return np.searchsorted(v, a), v


@nb.njit((nb.i8, nb.i8, nb.i8[:, :]), cache=True)
def solve(h: int, w: int, rca: np.ndarray) -> typing.NoReturn:
    n = len(rca)
    # rca = rca[np.argsort(rca[:, 2], kind='mergesort')]
    # b = np.empty(n, np.int64)
    # for i in range(n):
    #     r, c, a = rca[i]
    #     b[i] = r * w + c
    # v = np.unique(b)
    # idx = np.empty(n, np.int64)
    # for i in range(n): idx[np.searchsorted(v, b[i])] = i

    # dyx = ((-1, 0), (0, -1), (1, 0), (0, 1))

    # def on_board(y, x):
    #     return 0 <= y < h and 0 <= x < w

    g = np.empty((1 << 23, 2), np.int64)
    ptr = 0

    key = (rca[:, 0] << 30) + rca[:, 2]
    sort_idx = np.argsort(key, kind='mergesort')
    tmp = rca[sort_idx]
    original = np.arange(n)[sort_idx]
    for i in range(n - 1):
        if tmp[i + 1, 0] != tmp[i, 0]: continue
        if tmp[i + 1, 2] <= tmp[i, 2]: continue
        g[ptr] = (original[i], original[i + 1])
        ptr += 1


    key = (rca[:, 1] << 30) + rca[:, 2]
    sort_idx = np.argsort(key, kind='mergesort')
    tmp = rca[sort_idx]
    original = np.arange(n)[sort_idx]
    for i in range(n - 1):
        if tmp[i + 1, 1] != tmp[i, 1]: continue
        if tmp[i + 1, 2] <= tmp[i, 2]: continue
        g[ptr] = (original[i], original[i + 1])
        ptr += 1

    g = g[:ptr]
    g, edge_idx, _ = sort_csgraph(n, g)
    order = np.argsort(rca[:, 2])[::-1]
    visited = np.zeros(n, np.bool8)

    dist = np.zeros(n, np.int64)
    for u in order:
        for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
            dist[u] = max(dist[u], dist[v] + 1)
        # if visited[i]: continue
    # print(dist)
    for d in dist:
        print(d)

    # if visited[i]: continue
    # print(g)


def main() -> typing.NoReturn:
    h, w, n = map(int, input().split())
    rca = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 3)
    rca[:, :2] -= 1
    solve(h, w, rca)


main()
