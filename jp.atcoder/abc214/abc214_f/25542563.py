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
  prev = np.full(26, -1, np.int64)
  dp = np.zeros(1 << 18, np.int64)
  n = len(s)
  for i in range(n):
    j = prev[s[i]]
    dp[i + 1] = j == -1
    j -= j == i
    dp[i + 1] += dp[i - 1] - dp[j - 1]
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
    prev[s[i]] = i + 1
  print(dp[n] % mod)


def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('a')
  solve(s)


main()
