import typing
import sys
import functools
sys.setrecursionlimit(1 << 20)



def solve(a: typing.List[int]) -> typing.NoReturn:
  n = len(a)
  fixed_idx = [-1] * n
  fixed_val = [-1] * n
  for i in range(n):
    if a[i] == -1: continue
    fixed_idx[a[i]] = i
    fixed_val[i] = a[i]


  def can_transit(s, i):
    y, x = divmod(i, 5)
    if 1 <= y < 4 and (s >> i - 5 & 1) ^ (s >> i + 5 & 1):
      return False
    if 1 <= x < 4 and (s >> i - 1 & 1) ^ (s >> i + 1 & 1):
      return False
    return True


  mod = 1_000_000_007

  @functools.lru_cache(maxsize=None)
  def dp(s: int, v: int) -> int:
    if v < 0: return 1
    cnt = 0
    for i in range(n):
      if ~s >> i & 1: continue
      if fixed_idx[v] != -1 and fixed_idx[v] != i: continue
      if fixed_val[i] != -1 and fixed_val[i] != v: continue
      u = s & ~(1 << i)
      if not can_transit(u, i): continue
      cnt += dp(u, v - 1)
    return cnt % mod

  print(dp((1 << n) - 1, n - 1))


def main() -> typing.NoReturn:
  *a, = map(lambda x: int(x) - 1, sys.stdin.read().split())
  solve(a)


main()
