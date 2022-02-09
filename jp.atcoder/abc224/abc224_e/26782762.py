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

    dist = np.zeros(n, np.int64)
    qrmax = np.full(h, -1, np.int64)
    qcmax = np.full(w, -1, np.int64)
    prev = -1
    for i in np.argsort(rca[:, 2], kind='mergesort')[::-1]:
        r, c, a = rca[i]
        if a != prev:
            rmax = qrmax.copy()
            cmax = qcmax.copy()
        dist[i] = max(rmax[r], cmax[c]) + 1
        qrmax[r] = max(qrmax[r], dist[i])
        qcmax[c] = max(qcmax[c], dist[i])
        prev = a

    for d in dist:
        print(d)



def main() -> typing.NoReturn:
    h, w, n = map(int, input().split())
    rca = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 3)
    rca[:, :2] -= 1
    solve(h, w, rca)


main()
