import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def bit_count(
  n: int,
) -> np.array:
  a = np.zeros(n, np.int64)
  for i in range(n):
    a[i] = a[i // 2] + i % 2
  return a


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  a = a.astype(np.bool8)
  mod = 10 ** 9 + 7
  dp = np.zeros(
    1 << n,
    dtype=np.int64,
  )
  dp[0] = 1
  bitcnt = bit_count(1 << 22)

  i = np.arange(n)
  j = 1 << i
  for s in range((1 << n) - 1):
    c = bitcnt[s]
    ok = ~s >> i & 1 == 1
    ok &= a[c]
    k = s | j[ok]
    dp[k] += dp[s]
    dp[k] %= mod
  print(dp[-1])



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, n)
  solve(n, a)


main()
