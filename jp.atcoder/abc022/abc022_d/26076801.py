import typing
import sys
import numpy as np
import numba as nb


def solve(ab: np.ndarray) -> typing.NoReturn:
  g = np.mean(ab, axis=1)
  d = np.linalg.norm(ab - g[:, None], axis=-1)
  s = d.sum(axis=1)
  print(s[1] / s[0])


def main() -> typing.NoReturn:
  n = int(input())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(2, n, 2)
  solve(ab)


main()
