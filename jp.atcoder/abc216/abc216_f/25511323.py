import typing
import sys
import numpy as np



def main() -> typing.NoReturn:
  n = int(input())
  ab = map(
    int,
    sys.stdin.read().split(),
  )
  ab = zip(*zip(*[ab] * n))
  solve(ab)



def solve(
  ab: typing.Iterator[
    typing.Tuple[int, int]
  ],
) -> typing.NoReturn:
  mod = 998_244_353
  ab = sorted(ab)
  m = 1 << 13
  dp = np.zeros(m, dtype=np.int64)
  dp[0] = 1
  s = 0
  for a, b in ab:
    s += dp[:max(a - b + 1, 0)].sum()
    s %= mod
    dp[b:] += dp[:-b]
    dp %= mod
  print(s)


main()
