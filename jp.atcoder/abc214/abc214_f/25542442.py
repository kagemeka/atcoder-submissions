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
  prev = np.zeros(26, np.int64)
  dp = np.zeros(1 << 18, np.int64)
  dp[0] = dp[1] = 1
  n = len(s)
  for i in range(n):
    j = prev[s[i]]
    if j == i + 1: j -= 1
    dp[i + 2] = dp[i] - dp[j - 1]
    dp[i + 2] += dp[i + 1]
    dp[i + 2] %= mod
    prev[s[i]] = i + 2
  print((dp[n + 1] - 1) % mod)


def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('a')
  solve(s)


main()
