import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def sa_doubling(a: np.array) -> np.array:
    n = a.size
    rank, k = np.searchsorted(np.unique(a), a), 1
    while True:
        key = rank << 30
        key[:-k] |= 1 + rank[k:]
        sa = key.argsort(kind='mergesort')
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]])
        k <<= 1
        if k >= n: break
    return sa


@nb.njit
def lcp_array_kasai(a: np.array, sa: np.array) -> np.array:
    n = a.size
    assert n > 0 and sa.size == n
    rank = np.empty(n, np.int64)
    for i in range(n): rank[sa[i]] = i
    lcp, h = np.empty(n - 1, np.int64), 0
    for i in range(n):
        if h: h -= 1
        r = rank[i]
        if r == n - 1: continue
        j = sa[r + 1]
        while i + h < n and j + h < n and a[i + h] == a[j + h]: h += 1
        lcp[r] = h
    return lcp


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    sa = sa_doubling(a)
    lcp = lcp_array_kasai(a, sa)
    n = a.size
    print(n * (n + 1) // 2 - lcp.sum())



def main() -> typing.NoReturn:
    s = np.frombuffer(
        sys.stdin.buffer.readline().rstrip(),
        dtype='b',
    ).astype(np.int64) - ord('a') + 1
    solve(s)


main()
