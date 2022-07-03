# / mypy: ignore-errors
import typing


# M0 = 0x5555555555555555
# M1 = 0x3333333333333333
# M2 = 0x0F0F0F0F0F0F0F0F
# def popcount(n: int) -> int:
#     n -= (n >> 1) & M0
#     n = (n & M1) + ((n >> 2) & M1)
#     n = (n + (n >> 4)) & M2
#     n = n + (n >> 8)
#     n = n + (n >> 16)
#     n = n + (n >> 32)
#     return n & 0x7F


def popcount(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


K = 63


Self = typing.TypeVar("Self")


class BitArray:
    _d: typing.List[int]

    def __init__(self, size: int) -> None:
        self._d = [0] * ((size + M) >> K)

    def __getitem__(self, i: int) -> int:
        return self._d[i >> K] >> (i & M) & 1 == 1

    def __setitem__(self, i: int, value: int) -> None:
        if self[i] != value:
            self.flip(i)

    def flip(self, i: int) -> None:
        self._d[i >> K] ^= 1 << (i & M)

    def __and__(self, rhs: Self) -> Self:
        res = BitArray(0)
        res._d = self._d.copy()
        for i in range(min(len(self._d), len(rhs._d))):
            res._d[i] &= rhs._d[i]
        return res

    def and_count(self, rhs: Self) -> int:
        return sum(popcount(x & y) for x, y in zip(self._d, rhs._d))

    def popcount(self) -> int:
        return sum(popcount(x) for x in self._d)


def main() -> None:
    n = int(input())
    a = [BitArray(n) for _ in range(n)]
    for i in range(n):
        for j, v in enumerate(map(int, input())):
            a[i][j] = v

    cnt = 0
    for i in range(n):
        for j in range(i):
            if not a[i][j]:
                continue
            # cnt += (a[i] & a[j]).popcount()
            cnt += a[i].and_count(a[j])
    print(cnt // 3)


main()
