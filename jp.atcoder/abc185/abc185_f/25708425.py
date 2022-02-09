from __future__ import annotations
import typing



class FenwickTree():
  @classmethod
  def from_array(
    cls,
    a: typing.List[int],
  ) -> FenwickTree:
    n = len(a)
    a = a.copy()
    assert a[0] == 0
    for i in range(n):
      j = i + (i & -i)
      if j < n: a[j] ^= a[i]
    fw = cls(n)
    fw._FenwickTree__a = a
    return fw


  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * (n + 1)


  def __setitem__(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] ^= x
      i += i & -i


  def __getitem__(
    self,
    i: int,
  ) -> int:
    v = 0
    while i > 0:
      v ^= self.__a[i]
      i -= i & -i
    return v




def solve(
  a: typing.List[int],
  txy: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  fw = FenwickTree.from_array([0] + a)
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
