import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def next_permutation(a: np.ndarray) -> typing.NoReturn:
  n = a.size
  i = -1
  for j in range(n - 1, 0, -1):
    if a[j - 1] >= a[j]: continue
    i = j - 1
    break
  if i == -1:
    a[:] = -1
    return
  a[i + 1:] = a[i + 1:][::-1]
  for j in range(i + 1, n):
    if a[i] >= a[j]: continue
    a[i], a[j] = a[j], a[i]
    break


@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, xy: np.ndarray) -> typing.NoReturn:
  n = len(a)
  m = len(xy)
  ng_after = np.zeros(n, np.int64)
  for i in range(m):
    x, y = xy[i]
    ng_after[x] |= 1 << y
    ng_after[y] |= 1 << x

  def check_ok(perm):
    for i in range(n - 1):
      if ng_after[perm[i]] >> perm[i + 1] & 1: return False
    return True

  def total_time(perm):
    t = 0
    for i in range(n):
      t += a[perm[i], i]
    return t

  inf = 1 << 60
  mn = inf
  perm = np.arange(n)
  while perm[0] != -1:
    if check_ok(perm):
      mn = min(mn, total_time(perm))
    next_permutation(perm)

  if mn == inf:
    print(-1)
  else:
    print(mn)



def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  a = I[:n * n].reshape(n, n)
  xy = I[n * n + 1:].reshape(-1, 2) - 1
  solve(a, xy)


main()
