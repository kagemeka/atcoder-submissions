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
  prev = np.zeros(26, np.int64)
  dp = np.zeros(1 << 18, np.int64)
  dp[-1] = dp[0] = 1
  for i in range(n):
    dp[i + 1] = dp[i - 1] - dp[prev[s[i]] - 2]
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
    prev[s[i]] = i + 1
  print((dp[n] - 1) % mod)



def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('a')
  solve(s)


main()
