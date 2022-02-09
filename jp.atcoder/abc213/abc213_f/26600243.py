import typing
import numpy as np
import sys
import numba as nb


@nb.njit
def sa_is(a: np.ndarray) -> np.ndarray:
    def preprocess(a):
        n = a.size
        is_s = np.ones(n, np.bool8)
        for i in range(n - 2, -1, -1):
            is_s[i] = is_s[i + 1] if a[i] == a[i + 1] else a[i] < a[i + 1]
        is_lms = np.zeros(n, np.bool8)
        is_lms[1:][~is_s[:-1] & is_s[1:]] = True
        lms = np.flatnonzero(is_lms)
        bucket = np.bincount(a)
        return is_s, is_lms, lms, bucket

    def induce(a, is_s, lms, bucket):
        n, m = a.size, bucket.size
        sa = np.full(n, -1, np.int64)
        sa_idx = bucket.cumsum()
        for i in lms[::-1]:
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i

        sa_idx = bucket.copy()
        s = 0
        for i in range(m): s, sa_idx[i] = s + sa_idx[i], s
        for i in range(n):
            i = sa[i] - 1
            if i < 0 or is_s[i]: continue
            sa[sa_idx[a[i]]] = i
            sa_idx[a[i]] += 1

        sa_idx = bucket.cumsum()
        for i in range(n - 1, -1, -1):
            i = sa[i] - 1
            if i < 0 or not is_s[i]: continue
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i
        return sa

    def compute_lms_rank(a, sa, is_lms):
        n = a.size
        lms_idx = sa[is_lms[sa]]
        l = lms_idx.size
        rank = np.full(n, -1, dtype=np.int64)
        rank[-1] = r = 0
        for i in range(l - 1):
            i, j = lms_idx[i], lms_idx[i + 1]
            for d in range(n):
                i_is_lms = is_lms[i + d]
                j_is_lms = is_lms[j + d]
                if a[i + d] != a[j + d] or i_is_lms ^ j_is_lms:
                    r += 1
                    break
                if d > 0 and i_is_lms | j_is_lms: break
            rank[j] = r
        return rank[rank >= 0]

    a = np.hstack((a - a.min() + 1, np.array([0])))
    st: typing.List[typing.Tuple[np.ndarray]] = []
    while True:
        is_s, is_lms, lms, b = preprocess(a)
        sa = induce(a, is_s, lms, b)
        st.append((a, is_s, lms, b))
        a = compute_lms_rank(a, sa, is_lms)
        l = lms.size
        if a.max() < l - 1: continue
        lms_order = np.empty(l, np.int64)
        for i in range(l): lms_order[a[i]] = i
        break
    while st:
        a, is_s, lms, b = st.pop()
        lms_order = induce(a, is_s, lms[lms_order], b)
    return lms_order[1:]



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
    sa = sa_is(a)
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
