import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  h, w = a.shape
  m = 1 << 2
  dp = np.zeros((h, w, m), np.int64)
  if a[0, 0] <= 0:
    dp[0, 0, 1] += 1
  if a[0, 0] >= 0:
    dp[0, 0, 0] += 1
  for i in range(h - 1):
    if a[i + 1, 0] <= 0:
      dp[i + 1, 0, 1:] += dp[i, 0, :-1]
    if a[i + 1, 0] >= 0:
      dp[i + 1, 0] += dp[i, 0]

  for j in range(w - 1):
    if a[0, j + 1] <= 0:
      dp[0, j + 1, 1:] += dp[0, j, :-1]
    if a[0, j + 1] >= 0:
      dp[0, j + 1] += dp[0, j]
  dp %= mod

  for i in range(h - 1):
    for j in range(w - 1):
      # if a[i, j] == 1:
      if a[i + 1, j + 1] <= 0:
        dp[i + 1, j + 1, 1:] += (
          dp[i + 1, j, :-1] * dp[i, j + 1, :-1] % mod
        )
      if a[i + 1, j + 1] >= 0:
        dp[i + 1, j + 1] += dp[i + 1, j] * dp[i, j + 1] % mod
      dp[i + 1, j + 1] %= mod

  print(dp[-1, -1].sum() % mod)


def main() -> typing.NoReturn:
  h, w = map(int, sys.stdin.buffer.readline().split())
  s = np.frombuffer(
    sys.stdin.buffer.read(),
    dtype='S1',
  ).reshape(h, w + 1)[:, :-1]
  a = np.empty((h, w), np.int64)
  a[s == b'.'] = 0
  a[s == b'R'] = -1
  a[s == b'B'] = 1
  solve(a)


main()
