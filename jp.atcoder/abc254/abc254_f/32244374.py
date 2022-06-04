# mypy: ignore-errors


def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


import typing

T = typing.TypeVar("T")


class Semigroup(typing.Generic[T]):
    operation: typing.Callable[[T, T], T]

    def __init__(self, operation: typing.Callable[[T, T], T]) -> None:
        self.operation = operation


class Monoid(Semigroup[T]):
    identity: typing.Callable[[], T]

    def __init__(
        self, operation: typing.Callable[[T, T], T], identity: typing.Callable[[], T]
    ) -> None:
        super().__init__(operation)
        self.identity = identity


S = typing.TypeVar("S")
F = typing.TypeVar("F")


def sparse_table(
    semigroup: Semigroup[S],
    arr: typing.List[S],
) -> typing.Callable[[int, int], S]:
    n = len(arr)
    assert n > 0
    data = [arr.copy()]
    for i in range((n - 1).bit_length() - 1):
        data.append(data[i].copy())
        for j in range(n - (1 << i)):
            data[i + 1][j] = semigroup.operation(
                data[i][j],
                data[i][j + (1 << i)],
            )

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = (right - 1 - left).bit_length() - 1
        return semigroup.operation(data[k][left], data[k][right - (1 << k)])

    return get


import math
import operator


def main() -> None:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    da = [a[i + 1] - a[i] for i in range(n - 1)] + [0]
    db = [b[i + 1] - b[i] for i in range(n - 1)] + [0]

    monoid_s = Monoid(math.gcd, lambda: 0)
    sp_a = sparse_table(monoid_s, da)
    sp_b = sparse_table(monoid_s, db)

    res = []
    for _ in range(q):
        h0, h1, w0, w1 = map(int, input().split())
        h0 -= 1
        w0 -= 1
        g = a[h0] + b[w0]
        if h1 > h0 + 1:
            g = math.gcd(g, sp_a(h0, h1 - 1))
        if w1 > w0 + 1:
            g = math.gcd(g, sp_b(w0, w1 - 1))
        res.append(g)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
