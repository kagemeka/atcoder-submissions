import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def seg_build(n: int) -> typing.NoReturn:
  return np.zeros(n * 2, np.int64)


@nb.njit
def seg_build_from_array(a: np.ndarray) -> np.ndarray:
  n = len(a)
  seg = np.empty(n * 2, np.int64)
  seg[n:] = a
  for i in range(n - 1, 0, -1):
    seg[i] = seg[i << 1] ^ seg[i << 1 | 1]
  return seg


@nb.njit
def seg_set(
  seg: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  n = len(seg) >> 1
  i += n
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = seg[i << 1] ^ seg[i << 1 | 1]


@nb.njit
def seg_get(seg: np.ndarray, i: int) -> int:
  n = len(seg) >> 1
  return seg[i + n]


@nb.njit
def seg_get_range(seg: np.ndarray, l: int, r: int) -> int:
  n = len(seg) >> 1
  l, r = l + n, r + n
  v = 0
  while l < r:
    if l & 1:
      v ^= seg[l]
      l += 1
    if r & 1:
      r -= 1
      v ^= seg[r]
    l, r = l >> 1, r >> 1
  return v


@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(txy)
  seg = seg_build_from_array(a)
  for i in range(q):
    t, x, y = txy[i]
    if t == 1:
      x -= 1
      v = seg_get(seg, x)
      seg_set(seg, x, v ^ y)
    else:
      v = seg_get_range(seg, x - 1, y)
      print(v)


def main() -> typing.NoReturn:
  n, q = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  txy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(q, 3)

  solve(a, txy)


main()
