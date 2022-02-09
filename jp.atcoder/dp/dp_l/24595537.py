import typing
import numpy as np
import sys
import numba as nb

@nb.njit(
  (nb.i8, nb.i8[:]),
  cache=True,
)
def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  dp = np.zeros(
    (n + 1, n + 1),
    dtype=np.int64,
  )
  for w in range(1, n + 1):
    for l in range(n - w + 1):
      r = l + w
      x = dp[l + 1, r]
      y = dp[l, r - 1]
      if (n - w) & 1 ^ 1:
        dp[l, r] = max(
          x + a[l],
          y + a[r - 1],
        )
        continue
      dp[l, r] = min(
        x - a[l],
        y - a[r - 1],
      )

  print(dp[0, n])



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


main()
