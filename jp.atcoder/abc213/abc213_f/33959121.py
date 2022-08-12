import typing


L = typing.List


def lcp_array(a: L[int], sa: L[int]) -> L[int]:
    n = len(a)
    assert n > 0
    rank = [0] * n
    for i, j in enumerate(sa):
        rank[j] = i
    lcp, h = [0] * (n - 1), 0
    for i in range(n):
        if h > 0:
            h -= 1
        r = rank[i]
        if r == n - 1:
            continue
        j = sa[r + 1]
        while max(i, j) + h < n and a[i + h] == a[j + h]:
            h += 1
        lcp[r] = h
    return lcp


def suffix_array(a: typing.List[int]) -> typing.List[int]:
    n = len(a)
    d = 1
    sa = list(range(n))
    while True:
        for i in range(n):
            a[i] <<= 30
            if i + d < n:
                a[i] |= 1 + a[i + d]
        sa.sort(key=lambda i: a[i])
        d <<= 1
        if d >= n:
            return sa
        rank, prev = 0, a[sa[0]]
        for i in sa:
            if a[i] > prev:
                rank += 1
                prev = a[i]
            a[i] = rank
        if rank == n:
            return sa


def main() -> None:
    n = int(input())
    a = [ord(x) - ord("a") for x in input()]
    sa = suffix_array(a.copy())
    lcp = lcp_array(a, sa)

    a = list(range(n, 0, -1))
    for i in range(2):
        s = 0
        st = []
        for i in range(n - 1):
            l = 1
            h = lcp[i]
            while st and st[-1][0] >= h:
                x = st.pop()
                l += x[1]
                s -= x[0] * x[1]
            s += h * l
            st.append((h, l))
            a[sa[i + 1]] += s
        sa.reverse()
        lcp.reverse()
    print(*a, sep="\n")


main()
