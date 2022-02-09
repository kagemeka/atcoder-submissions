import typing
import sys
import numpy as np
import numba as nb
sys.setrecursionlimit(1 << 20)

def solve(n: int, d: int) -> typing.NoReturn:
  mod = 998244353
  b = [0] * n
  b[0] = 1
  b[1] = 1
  for i in range(1, n - 1):
    b[i + 1] = b[i] * 2 % mod

  cnt = [0] * n
  for i in range(n):
    j = d - i
    if j < 0 or j > n - 1: continue
    cnt[i] = b[i] * b[j] % mod
    # cnt[i] = 1
  s = cnt.copy()
  for i in range(n - 1):
    s[i + 1] += s[i]
    s[i + 1] %= mod

  res = [0] * n
  for depth in range(n - 2, -1, -1):
    r = d
    l = d - n + 1 + depth
    r = min(d, n - 1 - depth)
    l = max(l, 0)
    if r < l:
      tmp = 0
    else:
      tmp = s[r] - (s[l - 1] if l > 0 else 0)
    res[depth] = res[depth + 1] * 2 + tmp
    res[depth] %= mod
  print(res[0] * 2 % mod)


def main() -> typing.NoReturn:
  n, d = map(int, input().split())
  solve(n, d)


main()
