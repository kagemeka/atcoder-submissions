import typing
import sys
import numpy as np


def solve(ab: np.ndarray, cd: np.ndarray) -> typing.NoReturn:
  d = np.abs(ab[:, None] - cd[None, :]).sum(axis=-1)
  i = np.argmin(d, axis=-1) + 1
  print(*i, sep='\n')


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(-1, 2)
  ab = I[:n]
  cd = I[n:]
  solve(ab, cd)


main()
