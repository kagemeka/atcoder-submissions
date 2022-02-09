import typing


class Fenwick():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * n


  def __setitem__(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] += x
      i |= i + 1


  def __getitem__(
    self,
    i: int,
  ) -> int:
    s = 0
    while i >= 0:
      s += self.__a[i]
      i &= i + 1
      i -= 1
    return s



import sys

def main() -> typing.NoReturn:
  n, q = map(
    int, input().split(),
  )
  *a, = map(
    int, input().split(),
  )
  q = map(
    int,
    sys.stdin.read().split(),
  )
  fw = Fenwick(n)
  for i, x in enumerate(a):
    fw[i] = x


  for t, x, y in zip(*[q] * 3):
    if t == 0:
      fw[x] = y
      continue

    print(
      fw[y - 1] - fw[x - 1]
    )


main()
