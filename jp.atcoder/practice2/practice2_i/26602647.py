import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def sa_doubling_countsort(a: np.array) -> np.array:
    n = a.size
    def counting_sort(a):
        cnt = np.zeros(n + 2, dtype=np.int32)
        for x in a: cnt[x + 1] += 1
        for i in range(n): cnt[i + 1] += cnt[i]
        idx = np.empty(n, dtype=np.int32)
        for i in range(n):
            idx[cnt[a[i]]] = i
            cnt[a[i]] += 1
        return idx

    rank, k = np.searchsorted(np.unique(a), a), 1
    while True:
        second = np.zeros(n, dtype=np.int64)
        second[:-k] = 1 + rank[k:]
        rank_second = counting_sort(second)
        first = rank[rank_second]
        rank_first = counting_sort(first)
        sa = rank_second[rank_first]
        key = first[rank_first] << 30 | second[sa]
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[i + 1] > key[i])
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
    sa = sa_doubling_countsort(a)
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
