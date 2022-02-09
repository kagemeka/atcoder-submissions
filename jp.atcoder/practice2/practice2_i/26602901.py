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


def sa_doubling(a: typing.List[int]) -> typing.List[int]:
    n = len(a)
    rank, k = CompressArray()(a), 1
    while True:
        key = [r << 30 for r in rank]
        for i in range(n - k): key[i] |= 1 + rank[i + k]
        sa = sorted(range(n), key=lambda x: key[x])
        # sa = key.argsort(kind='mergesort')
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]])
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
  sa = sa_doubling(a)
  lcp = lcp_array_kasai(a, sa)
  print(n * (n + 1) // 2 - sum(lcp))


main()
