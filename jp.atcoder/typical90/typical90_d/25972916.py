import typing
import sys
import numpy as np


def solve(a: np.ndarray) -> typing.NoReturn:
  h, w = a.shape
  sy = a.sum(axis=0)
  sx = a.sum(axis=1)
  b = sx[:, None] + sy[None, :] - a
  for x in b:
    print(' '.join(map(str, x.tolist())))


def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(h, w)
  solve(a)


main()
