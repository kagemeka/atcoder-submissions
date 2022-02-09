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




S = typing.TypeVar('S')

@nb.njit
def seg_build(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  a: np.ndarray,
) -> np.ndarray:
  n = 1 << bit_length(len(a) - 1)
  seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
  seg[n:n + len(a)] = a.copy()
  for i in range(n + len(a), n << 1):
    seg[i] = e()
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
  l: int,
  r: int,
) -> int:
  return _seg_get(seg, op, e, l, r, 0, len(seg) >> 1, 1)


@nb.njit
def _seg_get(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  l: int,
  r: int,
  s: int,
  t: int,
  i: int,
) -> int:
  if t <= l or r <= s: return e()
  if l <= s and t <= r:
    return seg[i]
  c = (s + t) // 2
  vl = _seg_get(seg, op, e, l, r, s, c, i << 1)
  vr = _seg_get(seg, op, e, l, r, c, t, i << 1 | 1)
  return op(vl, vr)



@nb.njit((nb.i8[:], nb.i8[:, :]), cache=False)
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(txy)

  def seg_op(a, b):
    return a ^ b

  def seg_e():
    return 0

  seg = seg_build(seg_op, seg_e, a)
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
