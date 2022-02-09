import typing
import sys
import numpy as np


def solve(a: np.ndarray) -> typing.NoReturn:
  m = 1 << 10
  s = np.zeros((m, m), np.int64)
  l, d, r, u = a.T
  np.add.at(s, (d, l), 1)
  np.subtract.at(s, (d, r), 1)
  np.subtract.at(s, (u, l), 1)
  np.add.at(s, (u, r), 1)
  np.cumsum(s, out=s, axis=0)
  np.cumsum(s, out=s, axis=1)
  b = np.bincount(s.ravel(), minlength=len(a) + 1)
  print(*b[1:], sep='\n')


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 4)
  solve(a)

main()
