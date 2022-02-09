import typing
import sys
import numpy as np
import numba as nb
import re


@nb.njit
def sort_csgraph(n: int, g: np.ndarray) -> typing.Tuple[(np.ndarray, ) * 3]:
    key = (g[:, 0] << 30) + g[:, 1]
    sort_idx = np.argsort(key, kind='mergesort')
    g = g[sort_idx]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    return g, edge_idx


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
    m = len(g)
    g = np.vstack((g, g))
    g[m:, :2] = g[m:, 1::-1]
    return g


@nb.njit((nb.i4, nb.i4[:, :], nb.i4, nb.i2), cache=True)
def solve(n: int, g: np.ndarray, s: int, k: int) -> typing.NoReturn:
    g, edge_idx = sort_csgraph(n, csgraph_to_directed(g))
    a = np.array([s])
    for _ in range(k):
        b = []
        for x in a:
            for y in g[edge_idx[x]:edge_idx[x + 1], 1]:
                b.append(y)
        a = np.unique(np.array(b))
    print(len(a))


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    ab = np.array([list(map(int, input().split())) for _ in range(m)], dtype=np.int32) - 1
    s = input()
    k = s.index('g') + 1
    ptn = re.compile(r'^[^\d]*(\d+)[^\d]*$')
    m = re.match(ptn, s)
    s = int(m.groups()[0]) - 1
    solve(n, ab, s, k)

main()
