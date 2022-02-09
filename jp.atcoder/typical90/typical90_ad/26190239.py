import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def prime_factor_cnt(n: int) -> np.ndarray:
  s = np.ones(n, np.bool8)
  s[:2] = False
  cnt = np.zeros(n, np.int8)
  for i in range(n):
    if not s[i]: continue
    j = np.arange(i, n, i)
    s[j[1:]] = False
    cnt[j] += 1
  return cnt


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, k: int) -> typing.NoReturn:
  cnt = prime_factor_cnt(1 << 24)
  s = np.count_nonzero(cnt[2:n + 1] >= k)
  print(s)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  solve(n, k)


main()
