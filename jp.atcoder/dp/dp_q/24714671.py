import typing
import dataclasses


T = typing.TypeVar('T')
@dataclasses.dataclass
class Monoid(
  typing.Generic[T],
):
  f: typing.Callable[[T, T], T]
  e: typing.Callable[[], T]
  commutative: bool = False


T = typing.TypeVar('T')
class Fenwick(
  typing.Generic[T],
):
  def __setitem__(
    self,
    i: int,
    x: T,
  ) -> typing.NoReturn:
    m = self.__monoid
    a = self.__a
    while i < len(a):
      a[i] = m.f(a[i], x)
      i += i & -i


  def __getitem__(
    self,
    i: int,
  ) -> T:
    m = self.__monoid
    v = m.e()
    while i > 0:
      v = m.f(v, self.__a[i])
      i -= i & -i
    return v


  def __init__(
    self,
    monoid: Monoid[T],
    n: int,
  ):
    assert monoid.commutative
    self.__a = [
      monoid.e()
      for _ in range(n + 1)
    ]
    self.__monoid = monoid



def solve(
  n: int,
  h: typing.List[int],
  a: typing.List[int],
) -> typing.NoReturn:
  inf = 1 << 50
  monoid = Monoid[int](
    max,
    lambda : -inf,
    commutative=1,
  )
  fw = Fenwick(monoid, n)
  indices = sorted(
    range(n),
    key=lambda i: h[i],
  )
  for i in indices:
    v = fw[i]
    fw[i + 1] = max(
      v + a[i],
      a[i],
    )
  print(fw[n])



def main() -> typing.NoReturn:
  n = int(input())
  *h, = map(
    int, input().split(),
  )
  *a, = map(
    int, input().split(),
  )
  solve(n, h, a)


main()
