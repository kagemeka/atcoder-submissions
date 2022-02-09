import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  divisors_cnt = np.zeros(n, np.int64)
  for i in range(n):
    for j in range(n):
      divisors_cnt[i] += a[i] % a[j] == 0

  ex = 0
  for c in divisors_cnt:
    ex += ((c + 1) // 2) / c
  print(ex)


def main() -> typing.NoReturn:
  n = int(input())
  c = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(c)


main()
