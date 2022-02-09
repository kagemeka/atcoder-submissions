import typing
import sys
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def solve(
  s: np.ndarray,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  n = s.size
  dp = np.zeros(n, np.int64)
  for i in range(n):
    for j in range(i - 2, -1, -1):
      dp[i] += dp[j]
      if s[j + 1] == s[i]: break
    else:
      dp[i] += 1
    dp[i] %= mod
  print(dp.sum() % mod)


def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('a')
  solve(s)


main()
