import typing
import sys


class BitCnt():
  def __getitem__(
    self,
    n: int,
  ) -> int:
    return self.__a[n]

  def __call__(
    self,
    n: int,
  ) -> int:
    return self.__a[n]


  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    a = [0] * (n + 1)
    for i in range(n):
      a[i] = a[i // 2] + i % 2
    self.__a = a



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  dp = [0] * (1 << n)
  dp[0] = 1
  bitcnt = BitCnt(1 << 22)
  for s in range(1 << n):
    c = bitcnt[s]
    for i in range(n):
      if s >> i & 1: continue
      if a[c][i] == 0:
        continue
      t = s | 1 << i
      dp[t] += dp[s]
      dp[t] %= mod

  print(dp[-1])



def main() -> typing.NoReturn:
  n = int(input())
  a = [
    list(
      map(int, input().split())
    )
    for _ in range(n)
  ]
  solve(n, a)


main()
