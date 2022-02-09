import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def mod_fibonacci_sequence(n: int, mod: int) -> np.ndarray:
  assert n >= 2
  f = np.empty(n, np.int64)
  f[0], f[1] = 0, 1
  for i in range(2, n):
    f[i] = (f[i - 1] + f[i - 2]) % mod
  return f


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  mod = 10 ** 9 + 7
  fib = mod_fibonacci_sequence(n + 1, mod)
  dp = np.zeros((n + 1, 2), np.int64)
  for i in range(n):
    dp[i + 1, 0] = dp[i, 1] - fib[i] * a[i]
    dp[i + 1, 1] = dp[i].sum() + fib[i + 1] * a[i]
    dp[i + 1] %= mod
  print(dp[-1].sum() % mod)


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
