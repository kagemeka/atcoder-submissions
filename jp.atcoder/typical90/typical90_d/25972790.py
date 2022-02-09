import typing
import sys
import numpy as np
# import numba as nb


def solve(a: np.ndarray) -> typing.NoReturn:
  h, w = a.shape
  b = np.zeros((h, w), np.int64)
  b += a.cumsum(axis=0)
  b += a[::-1].cumsum(axis=0)[::-1]
  b += a.T.cumsum(axis=0).T
  b += a.T[::-1].cumsum(axis=0)[::-1].T
  b -= a * 3
  for x in list(b):
    print(' '.join(map(str, x.tolist())))


def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(h, w)
  solve(a)


main()
