import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def cumsum(a: np.ndarray) -> typing.NoReturn:
  for i in range(len(a) - 1): a[i + 1] += a[i]


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  h, w = a.shape
  b = np.zeros((h, w), np.int64)
  c = a.copy()
  cumsum(c)
  b += c
  c = a[::-1].copy()
  cumsum(c)
  b += c[::-1]
  c = a.copy().T
  cumsum(c)
  b += c.T
  c = a.copy().T[::-1]
  cumsum(c)
  b += c[::-1].T
  b -= a * 3
  return b


def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(h, w)
  b = solve(a)
  for x in list(b):
    print(*list(x))


main()
