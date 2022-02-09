import typing
import sys
import numpy as np
import numba as nb

@nb.njit
def uf_build(n: int) -> np.ndarray: return np.full(n, -1, np.int64)


@nb.njit
def uf_find(uf: np.ndarray, u: int) -> int:
    if uf[u] < 0: return u
    uf[u] = uf_find(uf, uf[u])
    return uf[u]


@nb.njit
def uf_unite(uf: np.ndarray, u: int, v: int) -> typing.NoReturn:
    u, v = uf_find(uf, u), uf_find(uf, v)
    if u == v: return
    if uf[u] > uf[v]: u, v = v, u
    uf[u] += uf[v]
    uf[v] = u


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
    n = len(xy)

    dist = np.zeros((n + 2, n + 2), np.float64)
    for i in range(n):
        for j in range(i):
            ix, iy = xy[i]
            jx, jy = xy[j]
            dist[i, j] = dist[j, i] = np.sqrt((jx - ix) ** 2 + (jy - iy) ** 2)
    for i in range(n):
        y = xy[i, 1]
        dist[i, n] = dist[n, i] = y + 100
        dist[i, n + 1] = dist[n + 1, i] = 100 - y
    dist[n, n + 1] = dist[n + 1, n] = 200

    def reachable(r):
        d = r * 2
        uf = uf_build(n + 2)
        for i in range(n + 2):
            for j in range(n + 2):
                if dist[i, j] >= d: continue
                uf_unite(uf, i, j)
        return uf_find(uf, n) != uf_find(uf, n + 1)

    def binary_search():
        lo, hi = 0, 200.1
        for _ in range(100):
            r = (lo + hi) / 2
            if reachable(r):
                lo = r
            else:
                hi = r
        return lo

    print(binary_search())

def main() -> typing.NoReturn:
    n = int(input())
    xy = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, 2)
    solve(xy)


main()
