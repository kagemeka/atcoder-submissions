import typing
import dataclasses


S = typing.TypeVar('S')
@dataclasses.dataclass
class Monoid(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
    e: typing.Callable[[], S]
    commutative: bool


S = typing.TypeVar('S')
class FenwickTree(typing.Generic[S]):
    def __init__(self, monoid: Monoid[S], a: list[S]) -> typing.NoReturn:
        n = len(a)
        fw = [None] * (n + 1)
        fw[1:] = a.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1: fw[j] = monoid.op(fw[j], fw[i])
        self.__m, self.__data = monoid, fw

    def __setitem__(self, i: int, x: S) -> typing.NoReturn:
        d = self.__data
        assert 0 <= i < len(d) - 1
        i += 1
        while i < len(d):
            d[i] = self.__m.op(d[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        m, d = self.__m, self.__data
        assert 0 <= i < len(d)
        v = m.e()
        while i > 0:
            v = m.op(v, d[i])
            i -= i & -i
        return v

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        m, d = self.__m, self.__data
        n = len(d)
        l = 1
        while l << 1 < n: l <<= 1
        v, i = m.e(), 0
        while l:
            if i + l < n and is_ok(m.op(v, d[i + l])):
                i += l
                v = m.op(v, d[i])
            l >>= 1
        return i


def solve(
  a: typing.List[int],
  txy: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  m = Monoid(lambda a, b: a ^ b, lambda: 0, True)
  fw = FenwickTree(m, a)
  res = []
  for t, x, y in txy:
    x -= 1
    if t == 1:
      fw[x] = y
    else:
      res.append(fw[y] ^ fw[x])
  print(*res, sep='\n')


import sys

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *a, = map(int, input().split())
  txy = map(int, sys.stdin.read().split())
  txy = zip(*[txy] * 3)
  solve(a, txy)


main()
