import typing


class CompressArray():
    def __call__(self, a: typing.List[int]) -> typing.NoReturn:
        from bisect import bisect_left
        v = sorted(set(a))
        self.__v = v
        return [bisect_left(v, x) for x in a]

    def __getitem__(self, i: int) -> int: return self.retrieve(i)
    def retrieve(self, i: int) -> int: return self.__v[i]



def sa_doubling_countsort(a: typing.List[int]) -> typing.List[int]:
    n = len(a)
    def counting_sort(a):
        cnt = [0] * (n + 2)
        for x in a: cnt[x + 1] += 1
        for i in range(n): cnt[i + 1] += cnt[i]
        idx = [0] * n
        for i in range(n):
            idx[cnt[a[i]]] = i
            cnt[a[i]] += 1
        return idx

    rank, k = CompressArray()(a), 1
    while True:
        second = [0] * n
        for i in range(n - k): second[i] = 1 + rank[i + k]
        rank_second = counting_sort(second)
        first = [rank[i] for i in rank_second]
        rank_first = counting_sort(first)
        sa = [rank_second[i] for i in rank_first]
        key = [first[i] << 30 | second[j] for i, j in zip(rank_first, sa)]
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[i + 1] > key[i])
        k <<= 1
        if k >= n: break
    return sa


def lcp_array_kasai(
    a: typing.List[int],
    sa: typing.List[int],
) -> typing.List[int]:
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


def solve(s: str) -> typing.NoReturn:
    n = len(s)
    a = [ord(x) - ord('a') for x in s]
    sa = sa_doubling_countsort(a)
    lcp = lcp_array_kasai(a, sa)

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
    print(*a, sep='\n')


def main() -> typing.NoReturn:
    n = int(input())
    solve(input())


main()
