import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  inf = 1 << 20

  odd_sum = np.zeros(n + 1, np.int64)
  even_sum = np.zeros(n + 1, np.int64)
  for i in range(n):
    if i & 1 ^ 1: odd_sum[i + 1] = a[i]
    else: even_sum[i + 1] = a[i]
  odd_sum = odd_sum.cumsum()
  even_sum = even_sum.cumsum()

  def compute_takahashi_score(i):
    i0 = i
    sa, sb = -inf, -inf
    for j in range(n):
      i = i0
      if i == j: continue
      if i > j: i, j = j, i
      if i & 1:
        a = even_sum[j + 1] - even_sum[i]
        b = odd_sum[j + 1] - odd_sum[i]
      else:
        a = odd_sum[j + 1] - odd_sum[i]
        b = even_sum[j + 1] - even_sum[i]
      if b <= sb: continue
      sa, sb = a, b
    return sa


  def compute_max_score():
    s = -inf
    for i in range(n):
      s = max(s, compute_takahashi_score(i))
    return s

  print(compute_max_score())


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
