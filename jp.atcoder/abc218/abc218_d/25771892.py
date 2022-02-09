import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def solve(
  xy: np.ndarray,
) -> typing.NoReturn:
  n = len(xy)
  sort_idx = np.argsort(xy[:, 1], kind='mergesort')
  xy = xy[sort_idx]
  sort_idx = np.argsort(xy[:, 0], kind='mergesort')
  xy = xy[sort_idx]
  x = xy[:, 0]
  y = xy[:, 1]
  x = np.searchsorted(np.unique(x), x)
  y = np.searchsorted(np.unique(y), y)

  c = np.zeros((x.max() + 1, y.max() + 1), np.int64)
  for i in range(n):
    c[x[i], y[i]] = 1


  s = 0
  for i in range(n):
    a = x[i]
    idx = np.searchsorted(x, a, side='right')
    if idx == n: continue
    b = x[idx]
    for j in range(i + 1, n):
      if x[j] > a: break
      for k in range(b, len(c)):
        s += c[k, y[i]] * c[k, y[j]]

  print(s)




def main() -> typing.NoReturn:
  n = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xy)



main()
