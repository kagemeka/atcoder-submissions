import typing
import sys


def sa_is(a: typing.List[int]) -> typing.List[int]:
    mn = min(a)
    a = [x - mn + 1 for x in a]
    a.append(0)
    n = len(a)
    m = max(a) + 1
    is_s = [True] * n
    for i in range(n - 2, -1, -1):
        is_s[i] = is_s[i + 1] if a[i] == a[i + 1] else a[i] < a[i + 1]
    is_lms = [not is_s[i - 1] and is_s[i] for i in range(n)]
    lms = [i for i in range(n) if is_lms[i]]
    bucket = [0] * m
    for x in a:
        bucket[x] += 1

    def induce() -> typing.List[int]:
        sa = [-1] * n
        sa_idx = bucket.copy()
        for i in range(m - 1): sa_idx[i + 1] += sa_idx[i]
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

        sa_idx = bucket.copy()
        for i in range(m - 1): sa_idx[i + 1] += sa_idx[i]
        for i in range(n - 1, -1, -1):
            i = sa[i] - 1
            if i < 0 or not is_s[i]: continue
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i
        return sa

    sa = induce()
    lms_idx = [i for i in sa if is_lms[i]]
    l = len(lms_idx)
    rank = [-1] * n
    rank[-1] = r = 0
    for i in range(l - 1):
        j, k = lms_idx[i], lms_idx[i + 1]
        for d in range(n):
            j_is_lms, k_is_lms = is_lms[j + d], is_lms[k + d]
            if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms:
                r += 1
                break
            if d > 0 and j_is_lms | k_is_lms: break
        rank[k] = r
    rank = [i for i in rank if i >= 0]
    if r == l - 1:
        lms_order = [-1] * l
        for i, r in enumerate(rank): lms_order[r] = i
    else:
        lms_order = sa_is(rank)
    lms = [lms[i] for i in lms_order]
    return induce()[1:]


def lcp_array_kasai(a: typing.List[int], sa: typing.List[int]) -> typing.List[int]:
    n = len(a)
    assert n > 0
    rank = [0] * n
    for i, j in enumerate(sa): rank[j] = i
    lcp, h = [0] * (n - 1), 0
    for i in range(n):
        if h > 0: h -= 1
        r = rank[i]
        if r == n - 1: continue
        j = sa[r + 1]
        while i + h < n and j + h < n and a[i + h] == a[j + h]: h += 1
        lcp[r] = h
    return lcp


def main() -> typing.NoReturn:
  a = [ord(c) - ord('a') for c in input()]
  n = len(a)
  sa = sa_is(a)
  lcp = lcp_array_kasai(a, sa)
  print(n * (n + 1) // 2 - sum(lcp))


main()
