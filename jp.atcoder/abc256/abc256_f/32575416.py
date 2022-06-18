# mypy: ignore-errors

import typing

mod = 998_244_353


class FwIntAdd:
    """faster than abstract one"""

    _d: typing.List[int]

    def __init__(self, a: typing.List[int]) -> None:
        n = len(a)
        a = [0] + a
        for i in range(n):
            j = i + (i & -i)
            if j <= n:
                a[j] += a[i]
                a[j] %= mod
        self._d = a

    def __len__(self) -> int:
        return len(self._d) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i < len(self) + 1:
            self._d[i] += x
            self._d[i] %= mod
            i += i & -i

    def __getitem__(self, i: int) -> int:
        v = 0
        while i > 0:
            v += self._d[i]
            v %= mod
            i -= i & -i
        return v


def main() -> None:
    # custom fenwick ?

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    fw0 = FwIntAdd([0] * n)
    fw1 = FwIntAdd([0] * n)
    fw2 = FwIntAdd([0] * n)

    for i in range(n):
        fw0[i] = a[i]
        fw1[i] = i * a[i] % mod
        fw2[i] = i * i % mod * a[i] % mod

    inv = pow(2, -1, mod)
    for _ in range(q):
        q = tuple(map(int, input().split()))
        if q[0] == 1:
            x, v = q[1:]
            x -= 1
            delta = v - a[x]
            fw0[x] = delta
            fw1[x] = x * delta % mod
            fw2[x] = x * x % mod * delta % mod
            a[x] = v
        else:
            x = q[1]
            x -= 1
            s = 0
            s += (x + 1) * (x + 2) % mod * fw0[x + 1] % mod
            s -= (2 * x + 3) % mod * fw1[x + 1] % mod
            s += fw2[x + 1]
            s *= inv
            s %= mod
            print(s)


if __name__ == "__main__":
    main()
