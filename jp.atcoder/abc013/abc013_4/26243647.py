import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:], nb.i8), cache=True)
def solve(n: int, a: np.ndarray, k: int) -> typing.NoReturn:
  b = np.arange(n)
  for i in a[::-1]:
    b[i], b[i + 1] = b[i + 1], b[i]
  a = b
  buf = np.empty(n, np.int32)
  buf_idx = 0
  root = np.full(n, -1, np.int32)
  size = np.zeros(n, np.int32)
  start_idx = np.empty(n, np.int32)
  order = np.empty(n, np.int32)
  for i in range(n):
    if root[i] != -1: continue
    start_idx[i] = buf_idx
    u, j = i, 0
    while True:
      root[u] = i
      order[u] = j
      j += 1
      buf[buf_idx] = u
      buf_idx += 1
      u = a[u]
      size[i] += 1
      if u == i: break

  for i in range(n):
    r = root[i]
    res = buf[start_idx[r] + (order[i] + k) % size[r]]
    print(res + 1)




def main() -> typing.NoReturn:
  n, m, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  ) - 1
  solve(n, a, k)


main()
