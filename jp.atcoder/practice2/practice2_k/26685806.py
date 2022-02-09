import typing
# import dataclasses


S = typing.TypeVar('S')
# @dataclasses.dataclass
# class Monoid(typing.Generic[S]):
#     op: typing.Callable[[S, S], S]
#     e: typing.Callable[[], S]
#     commutative: bool


class Monoid(typing.Generic[S]):
    def __init__(
        self,
        op: typing.Callable[[S, S], S],
        e: typing.Callable[[], S],
        commutative: bool,
    ) -> typing.NoReturn:
        self.op = op
        self.e = e
        self.commutative = commutative


S = typing.TypeVar('S')
F = typing.TypeVar('F')
class SegmentTreeLazy():
    def __init__(
        self,
        ms: Monoid[S],
        mf: Monoid[F],
        map_: typing.Callable[[F, S], S],
        a: typing.List[S],
    ) -> typing.NoReturn:
        size = len(a)
        n = 1 << (size - 1).bit_length()
        data = [ms.e() for _ in range(n << 1)]
        data[n:n + size] = a.copy()
        lazy = [mf.e() for _ in range(n)]
        self.__ms, self.__mf, self.__map = ms, mf, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1): self.__merge(i)

    def __len__(self) -> int: return len(self.__data)

    @property
    def size(self) -> int: return self.__size

    def __merge(self, i: int) -> typing.NoReturn:
        d = self.__data
        d[i] = self.__ms.op(d[i << 1], d[i << 1 | 1])

    def __apply(self, i: int, f: F) -> typing.NoReturn:
        d, lz = self.__data, self.__lazy
        d[i] = self.__map(f, d[i])
        if i < len(lz): lz[i] = self.__mf.op(f, lz[i])

    def __propagate(self, i: int) -> typing.NoReturn:
        lz = self.__lazy
        self.__apply(i << 1, lz[i])
        self.__apply(i << 1 | 1, lz[i])
        lz[i] = self.__mf.e()

    def set(self, l: int, r: int, f: F) -> typing.NoReturn:
        assert 0 <= l <= r <= self.size
        n = len(self) >> 1
        l, r = n + l, n + r
        h = n.bit_length()

        for i in range(h, 0, -1):
            if (l >> i) << i != l: self.__propagate(l >> i)
            if (r >> i) << i != r: self.__propagate((r - 1) >> i)

        l0, r0 = l, r
        while l < r:
            if l & 1: self.__apply(l, f); l += 1
            if r & 1: r -= 1; self.__apply(r, f)
            l, r = l >> 1, r >> 1

        l, r = l0, r0
        for i in range(1, h + 1):
            if (l >> i) << i != l: self.__merge(l >> i)
            if (r >> i) << i != r: self.__merge((r - 1) >> i)

    def get(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        n = len(self) >> 1
        l, r = n + l, n + r
        h = n.bit_length()

        for i in range(h, 0, -1):
            if (l >> i) << i != l: self.__propagate(l >> i)
            if (r >> i) << i != r: self.__propagate((r - 1) >> i)

        ms, d = self.__ms, self.__data
        vl, vr = ms.e(), ms.e()
        while l < r:
            if l & 1: vl = ms.op(vl, d[l]); l += 1
            if r & 1: r -= 1; vr = ms.op(d[r], vr)
            l, r = l >> 1, r >> 1
        return ms.op(vl, vr)

    def update(self, i: int, x: S) -> typing.NoReturn:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        h = n.bit_length()
        for j in range(h, 0, -1): self.__propagate(i >> j)
        self.__data[i] = x
        for j in range(1, h + 1): self.__merge(i >> j)


S = typing.TypeVar('S')
F = typing.TypeVar('F')
class SegmentTreeLazyDFS():
    def __init__(
        self,
        ms: Monoid[S],
        mf: Monoid[F],
        map_: typing.Callable[[F, S], S],
        a: typing.List[S],
    ) -> typing.NoReturn:
        size = len(a)
        n = 1 << (size - 1).bit_length()
        data = [ms.e() for _ in range(n << 1)]
        data[n:n + size] = a.copy()
        lazy = [mf.e() for _ in range(n)]
        self.__ms, self.__mf, self.__map = ms, mf, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1): self.__merge(i)

    def __len__(self) -> int: return len(self.__data)

    @property
    def size(self) -> int: return self.__size

    def __merge(self, i: int) -> typing.NoReturn:
        d = self.__data
        d[i] = self.__ms.op(d[i << 1], d[i << 1 | 1])

    def __apply(self, i: int, f: F) -> typing.NoReturn:
        d, lz = self.__data, self.__lazy
        d[i] = self.__map(f, d[i])
        if i < len(lz): lz[i] = self.__mf.op(f, lz[i])

    def __propagate(self, i: int) -> typing.NoReturn:
        lz = self.__lazy
        self.__apply(i << 1, lz[i])
        self.__apply(i << 1 | 1, lz[i])
        lz[i] = self.__mf.e()

    def set(self, l: int, r: int, f: F) -> typing.NoReturn:
        assert 0 <= l <= r <= self.size
        self.__set(l, r, f, 0, len(self) >> 1, 1)

    def __set(self, l: int, r: int, f: F, s: int, t: int, i: int) -> typing.NoReturn:
        n = len(self) >> 1
        if i < n: self.__propagate(i)
        if t <= l or r <= s: return
        if l <= s and t <= r:
            self.__apply(i, f)
            if i < n: self.__propagate(i)
            return
        c = (s + t) >> 1
        self.__set(l, r, f, s, c, i << 1)
        self.__set(l, r, f, c, t, i << 1 | 1)
        self.__merge(i)

    def get(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        return self.__get(l, r, 0, len(self) >> 1, 1)

    def __get(self, l: int, r: int, s: int, t: int, i: int) -> S:
        ms = self.__ms
        n = len(self) >> 1
        if i < n: self.__propagate(i)
        if t <= l or r <= s: return ms.e()
        if l <= s and t <= r:
            if i < n: self.__propagate(i)
            return self.__data[i]
        c = (s + t) >> 1
        vl = self.__get(l, r, s, c, i << 1)
        vr = self.__get(l, r, c, t, i << 1 | 1)
        self.__merge(i)
        return ms.op(vl, vr)

    def update(self, i: int, x: S) -> typing.NoReturn:
        assert 0 <= i < self.size
        n = len(self) >> 1
        a = self.get(i, i + 1)
        self.__data[n + i] = x
        a = self.get(i, i + 1)


MOD = 998_244_353


def e_s() -> S: return 0


def op_s(a: S, b: S) -> S:
    a1, a0 = divmod(a, 1 << 30)
    b1, b0 = divmod(b, 1 << 30)
    c0 = a0 + b0
    c1 = (a1 + b1) % MOD
    return (c1 << 30) + c0

def e_f() -> F: return 1 << 30

def op_f(f: F, g: F) -> F:
    f1, f0 = divmod(f, 1 << 30)
    g1, g0 = divmod(g, 1 << 30)
    h1 = f1 * g1 % MOD
    h0 = (f1 * g0 + f0) % MOD
    return (h1 << 30) + h0

def map_(f: F, x: S) -> S:
    f1, f0 = divmod(f, 1 << 30)
    x1, x0 = divmod(x, 1 << 30)
    y0 = x0
    y1 = (f1 * x1 + f0 * x0) % MOD
    return (y1 << 30) + y0


def solve(a: typing.List[int], q: typing.List[typing.Tuple[int]]) -> typing.NoReturn:
    ms = Monoid(op_s, e_s, True)
    mf = Monoid(op_f, e_f, False)
    b = [(x << 30) + 1 for x in a]
    seg = SegmentTreeLazyDFS(ms, mf, map_, b)
    for row in q:
        if row[0] == 0:
            l, r, b, c = row[1:]
            seg.set(l, r, (b << 30) + c)
        else:
            print(seg.get(*row[1:]) >> 30)


def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    q = [tuple(map(int, input().split())) for _ in range(q)]
    solve(a, q)

main()
