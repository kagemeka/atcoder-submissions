import typing
import sys
import numpy as np
import numba as nb





@nb.njit
def lpf(n: int) -> np.ndarray:
  s = np.arange(n)
  s[:2] = -1
  for i in range(n):
    if s[i] != i: continue
    j = np.arange(i, n, i)
    s[j[s[j] == j]] = i
  return s



@nb.njit((nb.i8, nb.i8), cache=True)
def solve(n: int, k: int) -> typing.NoReturn:
  a = lpf(1 << 24)

  def is_ok(x):
    cnt = 0
    p = -1
    while a[x] > 0:
      if a[x] != p:
        p = a[x]
        cnt += 1
      x //= a[x]
    return cnt >= k

  cnt = 0
  for i in range(2, n + 1):
    cnt += is_ok(i)

  print(cnt)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  solve(n, k)


main()
