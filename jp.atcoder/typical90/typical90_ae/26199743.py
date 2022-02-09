import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(w: np.ndarray, b: np.ndarray) -> typing.NoReturn:
  n = len(w)
  m = 50
  w_mx = m
  b_mx = m + m * (m + 1) // 2
  g = np.zeros((w_mx + 1, b_mx + 1), np.int64)
  cnt = np.zeros(b_mx // 2 + 1, np.int64)
  def compute_grundy(w, b):
    if w > 0: cnt[g[w - 1, b + w]] += 1
    for k in range(1, b // 2 + 1): cnt[g[w, b - k]] += 1
    mex = 0
    while cnt[mex]: mex += 1
    g[w, b] = mex
    for k in range(1, b // 2 + 1): cnt[g[w, b - k]] -= 1
    if w > 0 and b + w <= b_mx: cnt[g[w - 1, b + w]] -= 1

  for i in range(w_mx + 1):
    for j in range(b_mx - i * (i + 1) // 2 + 1):
      compute_grundy(i, j)

  v = 0
  for i in range(n):
    v ^= g[w[i], b[i]]

  ans = 'First' if v != 0 else 'Second'
  print(ans)


def main() -> typing.NoReturn:
  n = int(input())
  w = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(w, b)


main()
