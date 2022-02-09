import typing
import sys



class ModChoosePascal():
  def __call__(self, n: int, k: int) -> int:
    c = self.__c
    return c[n][k] if 0 <= k <= n < len(c) else 0


  def __init__(self, n: int, mod: int) -> typing.NoReturn:
    c = [[0] * n for _ in range(n)]
    for i in range(n): c[i][0] = 1
    for i in range(1, n):
      for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
    self.__c = c



def solve(
  r: int,
  c: int,
  x: int,
  y: int,
  d: int,
  l: int,
) -> typing.NoReturn:
  mod = 1_000_000_007
  choose = ModChoosePascal(1 << 10, mod)
  n = 4
  res = choose(x * y, d + l)
  for s in range(1, 1 << n):
    cnt = [0] * 2
    sign = -1
    for i in range(n):
      if ~s >> i & 1: continue
      cnt[i & 1] += 1
      sign *= -1
    if not (x - cnt[0] > 0 and y - cnt[1] > 0): continue
    res -= sign * choose((x - cnt[0]) * (y - cnt[1]), d + l)
    res %= mod
  res *= (r - x + 1) * (c - y + 1) * choose(l + d, d) % mod
  print(res % mod)



def main() -> typing.NoReturn:
  r, c = map(int, input().split())
  x, y = map(int, input().split())
  d, l = map(int, input().split())
  solve(r, c, x, y, d, l)


main()
