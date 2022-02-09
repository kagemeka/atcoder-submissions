import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def enumerate_fx() -> np.ndarray:
  a = np.array([1])
  for _ in range(12):
    b = []
    for x in a:
      for i in range(10):
        b.append(x * i)
    a = np.unique(np.array(b))
  return a

@nb.njit
def f(x: int) -> int:
  p = 1
  while x:
    x, r = divmod(x, 10)
    p *= r
  return p


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, b: int) -> typing.NoReturn:
  cands = enumerate_fx() + b
  cnt = 0
  for x in cands:
    cnt += 1 <= x <= n and x - f(x) == b
  print(cnt)


def main() -> typing.NoReturn:
  n, b = map(int, input().split())
  solve(n, b)


main()
