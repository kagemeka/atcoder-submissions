# / mypy: ignore-errors
import typing


def popcount(n: int) -> int:
    M0 = 0x5555555555555555
    M1 = 0x3333333333333333
    M2 = 0x0F0F0F0F0F0F0F0F
    n -= (n >> 1) & M0
    n = (n & M1) + ((n >> 2) & M1)
    n = (n + (n >> 4)) & M2
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x7F


K = 6
M = (1 << K) - 1


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
            cnt += (a[i] & a[j]).popcount()
    print(cnt // 3)


main()
