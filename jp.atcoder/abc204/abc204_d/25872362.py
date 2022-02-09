import typing
import sys
import numpy as np
import numba as nb



# @nb.njit((nb.i8[:], ), cache=True)
def solve(t: np.ndarray) -> typing.NoReturn:
  n = len(t)
  m = 1 << 17
  dp = np.zeros(m, np.bool8)
  dp[0] = True
  for x in t:
    dp[x:] |= dp[:-x]
  a = np.flatnonzero(dp)
  print(a)
  i = np.searchsorted(a, (t.sum() + 1) // 2)
  print(a[i])


def main() -> typing.NoReturn:
  n = int(input())
  t = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(t)


main()
