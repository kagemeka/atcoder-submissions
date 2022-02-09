import typing
import sys
import numpy as np



def enumerate_fx() -> np.ndarray:
  v = np.array([1])
  for _ in range(12):
    v = np.unique(v[:, None] * np.arange(10))
  return v


def f(n: int) -> int:
  p = 1
  while n:
    n, r = divmod(n, 10)
    p *= r
  return p


def solve(n: int, b: int) -> typing.NoReturn:
  cands = enumerate_fx() + b

  cnt = 0
  for x in cands.tolist():
    cnt += 1 <= x <= n and x - f(x) == b
  print(cnt)


def main() -> typing.NoReturn:
  n, b = map(int, input().split())
  solve(n, b)


main()
