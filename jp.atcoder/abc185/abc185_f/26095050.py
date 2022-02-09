import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def bit_length(n: int) -> int:
  l = 0
  while n:
    l += 1
    n >>= 1
  return l


@nb.njit
def seg_build(a: np.ndarray) -> np.ndarray:
  n = 1 << bit_length(len(a) - 1)
  seg = np.empty(n << 1, np.int64)
  seg[n:n + len(a)] = a
  for i in range(n - 1, 0, -1):
    seg[i] = seg[i << 1] ^ seg[i << 1 | 1]
  return seg


@nb.njit
def seg_set(
  seg: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  i += len(seg) >> 1
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = seg[i << 1] ^ seg[i << 1 | 1]


@nb.njit
def seg_get(seg: np.ndarray, l: int, r: int) -> int:
  return _seg_get(seg, l, r, 0, len(seg) >> 1, 1)


@nb.njit
def _seg_get(
  seg: np.ndarray,
  l: int,
  r: int,
  s: int,
  t: int,
  i: int,
) -> int:
  if t <= l or r <= s: return 0
  if l <= s and t <= r:
    return seg[i]
  c = (s + t) // 2
  vl = _seg_get(seg, l, r, s, c, i << 1)
  vr = _seg_get(seg, l, r, c, t, i << 1 | 1)
  return vl ^ vr



@nb.njit((nb.i8[:], nb.i8[:, :]))
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(txy)
  seg = seg_build(a)
  for i in range(q):
    t, x, y = txy[i]
    if t == 1:
      x -= 1
      v = seg_get(seg, x, x + 1)
      seg_set(seg, x, v ^ y)
    else:
      v = seg_get(seg, x - 1, y)
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
