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
  bitcnt = BitCnt(1 << 22)

  cache = [-1] * (1 << n)
  def dfs(
    s: int,
  ) -> int:
    if s == 0: return 1
    if cache[s] != -1:
      return cache[s]
    c = bitcnt[s]
    tot = 0
    for i in range(n):
      if ~s >> i & 1: continue
      if a[c - 1][i] == 0:
        continue
      tot += dfs(s - (1 << i))
    tot %= mod
    cache[s] = tot
    return tot


  print(dfs((1 << n) - 1))



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
