import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def int_to_digits(n: int) -> np.ndarray:
  digits = np.empty(20, np.int64)
  i = 0
  while n:
    n, r = divmod(n, 10)
    digits[i] = r
    i += 1
  return digits[:i]



@nb.njit
def count_ng(n: int) -> int:
  digits = int_to_digits(n)[::-1]
  dp = np.zeros(2, np.int64)
  dp[0] = 1
  for d in digits:
    dp[1] = dp[1] * 8 + dp[0] * (d - (d > 4))
    if d == 4 or d == 9:
      dp[0] = 0
  return n - dp.sum()


@nb.njit((nb.i8, nb.i8), cache=True)
def solve(a: int, b: int) -> typing.NoReturn:
  print(count_ng(b) - count_ng(a - 1))


def main() -> typing.NoReturn:
  a, b = map(int, input().split())
  solve(a, b)


main()
