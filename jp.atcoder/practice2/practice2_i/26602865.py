import typing
import sys


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


def main() -> typing.NoReturn:
  a = [ord(c) - ord('a') for c in input()]
  n = len(a)
  sa = sa_doubling_countsort(a)
  lcp = lcp_array_kasai(a, sa)
  print(n * (n + 1) // 2 - sum(lcp))


main()
