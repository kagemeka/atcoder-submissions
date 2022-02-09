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
    m = self.__monoid
    a = self.__a
    while i < len(a):
      a[i] = m.fn(a[i], x)
      i += i & -i



def solve(
  n: int,
  lrx: typing.Iterator[
    typing.Tuple[int],
  ],
) -> typing.NoReturn:
  lrx = sorted(lrx, key=lambda x: x[1])
  monoid = Monoid[int](
    fn=lambda x, y: x + y,
    e=lambda : 0,
    commutative=True,
  )
  fw = FenwickTree(monoid, 1 << 18)
  a = [0] * n
  st = []
  i = 0
  for l, r, x in lrx:
    while i < r:
      st.append(i)
      i += 1
    c = fw[r] - fw[l - 1]
    for _ in range(x - c):
      j = st.pop()
      fw[j + 1] = a[j] = 1
  print(*a)



import sys

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrx = map(int, sys.stdin.read().split())
  lrx = zip(*[lrx] * 3)
  solve(n, lrx)


main()
