import typing
import numpy as np
import sys
import numba as nb


@nb.njit
def sa_doubling(a: np.array) -> np.array:
    n = a.size
    cnt = np.empty(n + 1, dtype=np.int32)
    def counting_sort(a):
        cnt[:] = 0
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
        for i in range(n - k): second[i] = 1 + rank[i + k]
        rank_second = counting_sort(second)
        first = rank[rank_second]
        rank_first = counting_sort(first)
        sa = rank_second[rank_first]
        key = first[rank_first] << 30 | second[sa]
        rank = np.empty(n, np.int64)
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
def solve(a: np.array) -> typing.NoReturn:
    n = a.size
    sa = sa_doubling(a)
    lcp = lcp_array_kasai(a, sa)

    a = np.arange(n, 0, -1)
    for i in range(2):
        s = 0
        st = []
        for i in range(n - 1):
            h = lcp[i]
            l = 1
            while st and st[-1][0] >= h:
                x = st.pop()
                l += x[1]
                s -= x[0] * x[1]
            s += h * l
            st.append((h, l))
            a[sa[i + 1]] += s
        sa = sa[::-1]
        lcp = lcp[::-1]

    for i in range(n):
        print(a[i])


def main() -> typing.NoReturn:
    n = int(sys.stdin.buffer.readline().rstrip())
    a = np.frombuffer(
        sys.stdin.buffer.readline().rstrip(),
        dtype='b',
    ).astype(np.int64) - ord(b'a')
    solve(a)


main()
