import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(lr: np.ndarray, st: np.ndarray) -> typing.NoReturn:
  n, m = len(lr), len(st)
  res = np.full(m, -1, np.int64)
  for i in range(n):
    l, r = lr[i]
    for j in range(m):
      s, t = st[j]
      if s == t: continue
      if not l <= s <= r: continue
      if t < l:
        s = l
      elif t <= r:
        s = t
        res[j] = i + 1
      elif t > r:
        s = r
      st[j] = (s, t)
  for x in res:
    print(x)



def main() -> typing.NoReturn:
  n, d, k = map(int, input().split())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(-1, 2)
  lr = I[:d]
  st = I[d:]
  solve(lr, st)


main()
