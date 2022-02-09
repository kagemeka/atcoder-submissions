import typing
import sys


class BitCnt():

  def __call__(
    self,
    n: int,
  ) -> int:
    a = self.__a
    if n == 0: return 0
    if n in a: return a[n]
    c = self(n // 2) + n % 2
    a[n] = c
    return c


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__a = dict()


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  dp = [0] * (1 << n)
  dp[0] = 1
  bitcnt = BitCnt()
  for s in range(1 << n):
    c = bitcnt(s)
    for i in range(n):
      if ~s >> i & 1: continue
      if a[c - 1][i] == 0:
        continue
      dp[s] += dp[s - (1 << i)]
      dp[s] %= mod

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
