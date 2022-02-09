import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def longest_increasing_sequence(a: np.ndarray) -> np.ndarray:
  inf = 1 << 60
  assert inf > a.max()
  lis = np.full(len(a), inf, np.int64)
  for x in a:
    lis[np.searchsorted(lis, x)] = x
  return lis[:np.searchsorted(lis, inf)]


@nb.njit
def solve(a: np.ndarray) -> typing.NoReturn:
  lis = longest_increasing_sequence(a)
  print(len(a) - len(lis))


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a)


main()
