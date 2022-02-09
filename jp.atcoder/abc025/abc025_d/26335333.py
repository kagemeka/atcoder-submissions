import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def bit_count(n: int) -> int:
  cnt = 0
  while n:
    cnt += n & 1
    n >>= 1
  return cnt



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  fixed_idx = np.full(n, -1, np.int64)
  fixed_val = np.full(n, -1, np.int64)
  for i in range(n):
    if a[i] == -1: continue
    fixed_idx[a[i]] = i
    fixed_val[i] = a[i]

  def can_transit(s, i):
    y, x = divmod(i, 5)
    if 1 <= y <= 3 and (s >> (i - 5) & 1) ^ (s >> (i + 5) & 1):
      return False
    if 1 <= x <= 3 and (s >> (i - 1) & 1) ^ (s >> (i + 1) & 1):
      return False
    return True

  mod = 1_000_000_007
  dp = np.zeros(1 << n, np.int64)
  dp[0] = 1
  for s in range(1 << n):
    v = bit_count(s)
    for i in range(n):
      if s >> i & 1: continue
      if fixed_idx[v] != -1 and fixed_idx[v] != i: continue
      if fixed_val[i] != -1 and fixed_val[i] != v: continue
      if not can_transit(s, i): continue
      dp[s | 1 << i] = (dp[s | 1 << i] + dp[s]) % mod
  print(dp[-1])


def main() -> typing.NoReturn:
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ) - 1
  solve(a)


main()
