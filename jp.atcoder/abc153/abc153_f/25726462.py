import typing
import sys
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8[:, :], nb.i8, nb.i8),
  cache=True,
)
def solve(
  xh: np.ndarray,
  d: int,
  a: int,
) -> typing.NoReturn:
  n = len(xh)
  x = xh[:, 0]
  h = xh[:, 1]
  sort_idx = np.argsort(x, kind='mergesort')
  x, h = x[sort_idx], h[sort_idx]
  dh = np.zeros(n + 2, np.int64)
  cnt = 0
  r = 1
  for l in range(1, n + 1):
    dh[l] += dh[l - 1]
    h[l - 1] += dh[l]
    if h[l - 1] <= 0: continue
    while r - 1 < n and x[r - 1] - x[l - 1] <= 2 * d:
      r += 1
    c = (h[l - 1] + a - 1) // a
    cnt += c
    v = c * a
    dh[l] -= v
    dh[r] += v
  print(cnt)


def main() -> typing.NoReturn:
  n, d, a = map(int, input().split())
  xh = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xh, d, a)


main()
