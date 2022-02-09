from __future__ import annotations
import typing
import dataclasses





T = typing.TypeVar('T')
@dataclasses.dataclass
class Monoid(typing.Generic[T]):
  fn: typing.Callable[[T, T], T]
  e: typing.Callable[[], T]
  commutative: bool = False




T = typing.TypeVar('T')
class FenwickTree(typing.Generic[T]):
  @classmethod
  def from_array(
    cls,
    monoid: Monoid[T],
    a: typing.List[T],
  ) -> FenwickTree[T]:
    n = len(a)
    a = a.copy()
    assert a[0] == monoid.e()
    for i in range(n):
      j = i + (i & -i)
      if j >= n: continue
      a[j] = monoid.fn(a[j], a[i])
    fw = cls(monoid, n)
    fw._FenwickTree__a = a
    return fw


  def __getitem__(
    self,
    i: int,
  ) -> T:
    m = self.__monoid
    v = m.e()
    while i > 0:
      v = m.fn(v, self.__a[i])
      i -= i & -i
    return v


  def __init__(
    self,
    monoid: Monoid[T],
    n: int,
  ) -> typing.NoReturn:
    assert monoid.commutative
    self.__a = [monoid.e() for _ in range(n + 1)]
    self.__monoid = monoid


  def __setitem__(
    self,
    i: int,
    x: T,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] = self.__monoid.fn(a[i], x)
      i += i & -i



def solve(
  a: typing.List[int],
  txy: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  monoid = Monoid[int](
    fn=lambda x, y: x ^ y,
    e=lambda: 0,
    commutative=True,
  )
  fw = FenwickTree.from_array(monoid, [0] + a)
  res = []
  for t, x, y in txy:
    if t == 1:
      fw[x] = y
    else:
      res.append(fw[y] ^ fw[x - 1])
  print(*res, sep='\n')


import sys

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *a, = map(int, input().split())
  txy = map(int, sys.stdin.read().split())
  txy = zip(*[txy] * 3)
  solve(a, txy)


main()
