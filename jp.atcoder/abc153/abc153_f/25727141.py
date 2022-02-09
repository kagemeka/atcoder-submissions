import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def fw_build_from_array(
  a: np.ndarray,
) -> np.ndarray:
  assert a[0] == 0
  fw = a.copy()
  n = len(fw)
  for i in range(n):
    j = i + (i & -i)
    if j < n: fw[j] += fw[i]
  return fw



@nb.njit
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] += x
    i += i & -i


@nb.njit
def fw_get(
  fw: np.ndarray,
  i: int,
) -> int:
  v = 0
  while i > 0:
    v += fw[i]
    i -= i & -i
  return v



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
  x = np.hstack((np.array([-1]), xh[:, 0]))
  h = np.hstack((np.array([0]), xh[:, 1]))
  sort_idx = np.argsort(x, kind='mergesort')
  x, h = x[sort_idx], h[sort_idx]
  for i in range(n, 0, -1):
    h[i] -= h[i - 1]
  fw = fw_build_from_array(h)
  cnt = 0
  r = 1
  for l in range(1, n + 1):
    v = fw_get(fw, l)
    if v <= 0: continue
    while r <= n and x[r] - x[l] <= 2 * d:
      r += 1
    c = (v + a - 1) // a
    cnt += c
    v = c * a
    fw_set(fw, l, -v)
    fw_set(fw, r, v)
  print(cnt)


def main() -> typing.NoReturn:
  n, d, a = map(int, input().split())
  xh = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(xh, d, a)


main()
