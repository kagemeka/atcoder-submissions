import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__bit_code = """
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x
"""

atcoder._bit = types.ModuleType('atcoder._bit')
exec(_atcoder__bit_code, atcoder._bit.__dict__)


_atcoder_lazysegtree_code = """
import typing

# import atcoder._bit


class LazySegTree:
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(self, left: int, right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(
            self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id
"""

atcoder.lazysegtree = types.ModuleType('atcoder.lazysegtree')
atcoder.lazysegtree.__dict__['atcoder'] = atcoder
atcoder.lazysegtree.__dict__['atcoder._bit'] = atcoder._bit
exec(_atcoder_lazysegtree_code, atcoder.lazysegtree.__dict__)
LazySegTree = atcoder.lazysegtree.LazySegTree


_atcoder__math_code = """
import typing


def _is_prime(n: int) -> bool:
    '''
    Reference:
    M. Forisek and J. Jancina,
    Fast Primality Testing for Integers That Fit into a Machine Word
    '''

    if n <= 1:
        return False
    if n == 2 or n == 7 or n == 61:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in (2, 7, 61):
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
    a %= b
    if a == 0:
        return (b, 0)

    # Contracts:
    # [1] s - m0 * a = 0 (mod b)
    # [2] t - m1 * a = 0 (mod b)
    # [3] s * |m1| + t * |m0| <= b
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

        # [3]:
        # (s - t * u) * |m1| + t * |m0 - m1 * u|
        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
        # = s * |m1| + t * |m0| <= b

        s, t = t, s
        m0, m1 = m1, m0

    # by [3]: |m0| <= b/g
    # by g != b: |m0| < b/g
    if m0 < 0:
        m0 += b // s

    return (s, m0)


def _primitive_root(m: int) -> int:
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3

    divs = [2] + [0] * 19
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2

    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2

    if x > 1:
        divs[cnt] = x
        cnt += 1

    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                break
        else:
            return g
        g += 1
"""

atcoder._math = types.ModuleType('atcoder._math')
exec(_atcoder__math_code, atcoder._math.__dict__)


_atcoder_modint_code = """
import typing

# import atcoder._math


class ModContext:
    context: typing.List[int] = []

    def __init__(self, mod: int) -> None:
        assert 1 <= mod

        self.mod = mod

    def __enter__(self) -> None:
        self.context.append(self.mod)

    def __exit__(self, exc_type: typing.Any, exc_value: typing.Any,
                 traceback: typing.Any) -> None:
        self.context.pop()

    @classmethod
    def get_mod(cls) -> int:
        return cls.context[-1]


class Modint:
    def __init__(self, v: int = 0) -> None:
        self._mod = ModContext.get_mod()
        if v == 0:
            self._v = 0
        else:
            self._v = v % self._mod

    def mod(self) -> int:
        return self._mod

    def val(self) -> int:
        return self._v

    def __iadd__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            self._v += rhs._v
        else:
            self._v += rhs
        if self._v >= self._mod:
            self._v -= self._mod
        return self

    def __isub__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            self._v -= rhs._v
        else:
            self._v -= rhs
        if self._v < 0:
            self._v += self._mod
        return self

    def __imul__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            self._v = self._v * rhs._v % self._mod
        else:
            self._v = self._v * rhs % self._mod
        return self

    def __ifloordiv__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = atcoder._math._inv_gcd(rhs, self._mod)[1]
        self._v = self._v * inv % self._mod
        return self

    def __pos__(self) -> 'Modint':
        return self

    def __neg__(self) -> 'Modint':
        return Modint() - self

    def __pow__(self, n: int) -> 'Modint':
        assert 0 <= n

        return Modint(pow(self._v, n, self._mod))

    def inv(self) -> 'Modint':
        eg = atcoder._math._inv_gcd(self._v, self._mod)

        assert eg[0] == 1

        return Modint(eg[1])

    def __add__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            result = self._v + rhs._v
            if result >= self._mod:
                result -= self._mod
            return raw(result)
        else:
            return Modint(self._v + rhs)

    def __sub__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            result = self._v - rhs._v
            if result < 0:
                result += self._mod
            return raw(result)
        else:
            return Modint(self._v - rhs)

    def __mul__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            return Modint(self._v * rhs._v)
        else:
            return Modint(self._v * rhs)

    def __floordiv__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = atcoder._math._inv_gcd(rhs, self._mod)[1]
        return Modint(self._v * inv)

    def __eq__(self, rhs: typing.Union['Modint', int]) -> bool:  # type: ignore
        if isinstance(rhs, Modint):
            return self._v == rhs._v
        else:
            return self._v == rhs

    def __ne__(self, rhs: typing.Union['Modint', int]) -> bool:  # type: ignore
        if isinstance(rhs, Modint):
            return self._v != rhs._v
        else:
            return self._v != rhs


def raw(v: int) -> Modint:
    x = Modint()
    x._v = v
    return x
"""

atcoder.modint = types.ModuleType('atcoder.modint')
atcoder.modint.__dict__['atcoder'] = atcoder
atcoder.modint.__dict__['atcoder._math'] = atcoder._math
exec(_atcoder_modint_code, atcoder.modint.__dict__)
ModContext = atcoder.modint.ModContext

Modint = atcoder.modint.Modint

# https://atcoder.jp/contests/practice2/tasks/practice2_k

import sys
from typing import Tuple

# from atcoder.lazysegtree import LazySegTree
# from atcoder.modint import ModContext, Modint


def main() -> None:
    with ModContext(998244353):
        n, q = map(int, sys.stdin.readline().split())
        a = [(Modint(ai), 1) for ai in map(int, sys.stdin.readline().split())]

        def op(x: Tuple[Modint, int],
               y: Tuple[Modint, int]) -> Tuple[Modint, int]:
            return x[0] + y[0], x[1] + y[1]

        e = Modint(0), 0

        def mapping(x: Tuple[Modint, Modint],
                    y: Tuple[Modint, int]) -> Tuple[Modint, int]:
            return x[0] * y[0] + x[1] * y[1], y[1]

        def composition(x: Tuple[Modint, Modint],
                        y: Tuple[Modint, Modint]) -> Tuple[Modint, Modint]:
            return x[0] * y[0], x[0] * y[1] + x[1]

        id_ = Modint(1), Modint(0)

        lazy_segtree = LazySegTree(op, e, mapping, composition, id_, a)

        for _ in range(q):
            t, *inputs = map(int, sys.stdin.readline().split())
            if t == 0:
                l, r, b, c = inputs
                lazy_segtree.apply(l, r, (Modint(b), Modint(c)))
            else:
                l, r = inputs
                print(lazy_segtree.prod(l, r)[0].val())


if __name__ == '__main__':
    main()
