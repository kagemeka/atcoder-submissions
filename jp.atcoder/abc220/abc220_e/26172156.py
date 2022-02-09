import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, d: int) -> typing.NoReturn:
  mod = 998_244_353
  m = 1 << 21
  one_side_cnt_for_depth = np.ones(m, np.int64)
  c = one_side_cnt_for_depth
  for i in range(2, n): c[i] = c[i - 1] * 2 % mod
  pair_cnt = np.zeros(m, np.int64)
  for i in range(n):
    pair_cnt[i] = c[i] * c[d - i] % mod
  s = pair_cnt.cumsum() % mod
  s[-1] = 0

  res = np.zeros(n, np.int64)
  for depth in range(n - 2, -1, -1):
    res[depth] = res[depth + 1] * 2 % mod
    r = min(d, n - 1 - depth)
    l = max(d - n + 1 + depth, 0)
    if r < l: continue
    res[depth] += s[r] - s[l - 1]
  print(res[0] * 2 % mod)


def main() -> typing.NoReturn:
  n, d = map(int, input().split())
  solve(n, d)


main()
