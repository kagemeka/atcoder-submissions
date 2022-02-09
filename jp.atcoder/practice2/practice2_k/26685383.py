import typing
import dataclasses


S = typing.TypeVar('S')
@dataclasses.dataclass
class Monoid(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
    e: typing.Callable[[], S]
    commutative: bool


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


MOD = 998_344_353


def e_s() -> S:
    return (0, 0)


def op_s(a: S, b: S) -> S:
    return ((a[0] + b[0]) % MOD, a[1] + b[1])


def e_f() -> F:
    return (1, 0)

def op_f(f: F, g: F) -> F:
    return (f[0] * g[0] % MOD, (f[0] * g[1] + f[1]) % MOD)


def map_(f: F, x: S) -> S:
    return ((f[0] * x[0] + f[1] * x[1]) % MOD, x[1])

def solve(a: typing.List[int], q: typing.List[typing.Tuple[int]]) -> typing.NoReturn:
    ms = Monoid(op_s, e_s, True)
    mf = Monoid(op_f, e_f, False)
    b = [(x, 1) for x in a]
    seg = SegmentTreeLazy(ms, mf, map_, b)
    for row in q:
        if row[0] == 0:
            l, r, b, c = row[1:]
            seg.set(l, r, (b, c))
        else:
            print(seg.get(*row[1:])[0])


def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    q = [tuple(map(int, input().split())) for _ in range(q)]
    solve(a, q)

main()
