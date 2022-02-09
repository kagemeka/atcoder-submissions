import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def uf_build(n: int) -> np.ndarray:
    return np.full(n, -1, np.int64)

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


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, ab: np.ndarray) -> typing.NoReturn:
    m = len(ab)
    uf = uf_build(n)
    for i in range(m):
        a, b = ab[i]
        uf_unite(uf, a, b)

    root = np.empty(n, np.int64)
    for i in range(n): root[i] = uf_find(uf, i)
    print(np.sum(root == np.arange(n)) - 1)


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    ab = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(m, 2)
    solve(n, ab - 1)


main()
