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


class LazySegmentTree(typing.Generic[S, F]):
    _monoid_s: Monoid[S]
    _monoid_f: Monoid[F]
    _data: typing.List[S]
    _lazy: typing.List[F]
    _size: int

    def __init__(
        self,
        monoid_s: Monoid[S],
        monoid_f: Monoid[F],
        map_: typing.Callable[[F, S], S],
        arr: typing.List[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid_s.identity() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        lazy = [monoid_f.identity() for _ in range(n)]
        self._monoid_s, self._monoid_f, self.__map = monoid_s, monoid_f, map_
        self._size, self._data, self._lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self._merge(i)

    def __len__(self) -> int:
        return len(self._data)

    @property
    def size(self) -> int:
        return self._size

    def _merge(self, i: int) -> None:
        self._data[i] = self._monoid_s.operation(
            self._data[i << 1],
            self._data[i << 1 | 1],
        )

    def _apply(self, i: int, f: F) -> None:
        self._data[i] = self.__map(f, self._data[i])
        if i < len(self._lazy):
            self._lazy[i] = self._monoid_f.operation(f, self._lazy[i])

    def _propagate(self, i: int) -> None:
        self._apply(i << 1, self._lazy[i])
        self._apply(i << 1 | 1, self._lazy[i])
        self._lazy[i] = self._monoid_f.identity()

    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left += n
        right += n
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self._propagate(left >> i)
            if (right >> i) << i != right:
                self._propagate((right - 1) >> i)

        l0, r0 = left, right  # backup
        while left < right:
            if left & 1:
                self._apply(left, f)
                left += 1
            if right & 1:
                right -= 1
                self._apply(right, f)
            left, right = left >> 1, right >> 1

        left, right = l0, r0
        for i in range(1, height + 1):
            if (left >> i) << i != left:
                self._merge(left >> i)
            if (right >> i) << i != right:
                self._merge((right - 1) >> i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left, right = n + left, n + right
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self._propagate(left >> i)
            if (right >> i) << i != right:
                self._propagate((right - 1) >> i)

        vl, vr = self._monoid_s.identity(), self._monoid_s.identity()
        while left < right:
            if left & 1:
                vl = self._monoid_s.operation(vl, self._data[left])
                left += 1
            if right & 1:
                right -= 1
                vr = self._monoid_s.operation(self._data[right], vr)
            left, right = left >> 1, right >> 1
        return self._monoid_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        height = n.bit_length()
        for j in range(height, 0, -1):
            self._propagate(i >> j)
        self._data[i] = x
        for j in range(1, height + 1):
            self._merge(i >> j)


import math
import operator


def main() -> None:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    monoid_s = Monoid(math.gcd, lambda: 0)
    monoid_f = Monoid(operator.add, lambda: 0)
    map_ = operator.add

    seg_a = LazySegmentTree(monoid_s, monoid_f, map_, a)
    seg_b = LazySegmentTree(monoid_s, monoid_f, map_, b)

    res = []
    for _ in range(q):
        h0, h1, w0, w1 = map(int, input().split())
        h0 -= 1
        w0 -= 1
        seg_a.set(h0, h1, b[w0])
        seg_b.set(w0, w1, a[h0])
        g = math.gcd(seg_a.get(h0, h1), seg_b.get(w0, w1))
        seg_a.set(h0, h1, -b[w0])
        seg_b.set(w0, w1, -a[h0])
        res.append(g)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
