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
  dp = np.zeros(n + 3, np.int64)
  dp[0] = 1
  for i in range(n):
    for j in range(i - 1, -1, -1):
      dp[i + 2] += dp[j + 1]
      if s[j] == s[i]: break
    else:
      dp[i + 2] += 1
    dp[i + 2] %= mod
  print(dp[2:].sum())



def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('a')
  solve(s)


main()
