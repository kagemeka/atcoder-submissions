import typing
import sys
import numpy as np
import numba as nb

S = typing.TypeVar('S')

@nb.njit
def seg_build(
  op: typing.Callable[[S, S], S],
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
  seg[n:] = a.copy()
  for i in range(n - 1, 0, -1):
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])
  return seg


@nb.njit
def seg_set(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  i: int,
  x: int,
) -> typing.NoReturn:
  i += len(seg) >> 1
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])


@nb.njit
def seg_get(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  l: int, r: int) -> int:
  n = len(seg) >> 1
  l, r = l + n, r + n
  vl = vr = e()
  while l < r:
    if l & 1:
      vl = op(vl, seg[l])
      l += 1
    if r & 1:
      r -= 1
      vr = op(seg[r], vr)
    l, r = l >> 1, r >> 1
  return op(vl, vr)



@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(txy)

  def seg_op(a, b):
    return a ^ b

  def seg_e():
    return 0

  seg = seg_build(seg_op, a)
  for i in range(q):
    t, x, y = txy[i]
    if t == 1:
      x -= 1
      v = seg_get(seg, seg_op, seg_e, x, x + 1)
      seg_set(seg, seg_op, x, v ^ y)
    else:
      v = seg_get(seg, seg_op, seg_e, x - 1, y)
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
