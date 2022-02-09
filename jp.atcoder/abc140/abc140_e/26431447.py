# multiset with segment tree
import typing
import sys
import numpy as np
import numba as nb

@nb.njit
def bit_length(n: int) -> int:
  l = 0
  while 1 << l <= n: l += 1
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
  for i in range(n << 1): seg[i] = e()
  seg[n:n + len(a)] = a.copy()
  for i in range(n - 1, 0, -1):
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])
  return seg


@nb.njit
def seg_set(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  i: int,
  x: S,
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
  n = len(seg) >> 1
  l, r = l + n, r + n
  vl, vr = e(), e()
  while l < r:
    if l & 1:
      vl = op(vl, seg[l])
      l += 1
    if r & 1:
      r -= 1
      vr = op(seg[r], vr)
    l, r = l >> 1, r >> 1
  return op(vl, vr)


@nb.njit
def seg_max_right(
  op: np.ndarray,
  e: np.ndarray,
  seg: np.ndarray,
  is_ok: typing.Callable[[S], bool],
  x: S,
  l: int,
  size: int,
) -> int:
  n = len(seg) >> 1
  assert 0 <= l < size
  i = l + n
  v = e()
  while True:
    i //= i & -i
    if is_ok(op(v, seg[i]), x):
      v = op(v, seg[i])
      i += 1
      if i & -i == i: return size
      continue
    while i < n:
      i <<= 1
      if not is_ok(op(v, seg[i]), x): continue
      v = op(v, seg[i])
      i += 1
    return i - n




S = typing.TypeVar('S')
@nb.njit
def build_seg(a: np.ndarray) -> np.ndarray:
  return seg_build(seg_op, seg_e, a)


@nb.njit
def set_seg(seg: np.ndarray, i: int, x: S) -> typing.NoReturn:
  seg_set(seg, seg_op, i, x)


@nb.njit
def get_seg(seg: np.ndarray, l: int, r: int) -> S:
  return seg_get(seg, seg_op, seg_e, l, r)


@nb.njit
def operate_seg(
  seg: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  set_seg(seg, i, seg_op(get_seg(seg, i, i + 1), x))


@nb.njit
def max_right_seg(
  seg: np.ndarray,
  is_ok: typing.Callable[[S], bool],
  x: S,
  l: int,
  size: int,
) -> int:
  return seg_max_right(seg_op, seg_e, seg, is_ok, x, l, size)




# use with coordinates compression.


@nb.njit
def seg_op(a: S, b: S) -> S: return a + b


@nb.njit
def seg_e() -> S: return 0


@nb.njit
def ms_build(n: int) -> np.ndarray:
  return build_seg(np.zeros(n, np.int64))


@nb.njit
def ms_size(ms: np.ndarray) -> int:
  return get_seg(ms, 0, len(ms) - 1)

@nb.njit
def ms_add(ms: np.ndarray, x: int) -> typing.NoReturn:
  operate_seg(ms, x, 1)


@nb.njit
def ms_pop(ms: np.ndarray, x: int) -> typing.NoReturn:
  assert get_seg(ms, x, x + 1) > 0
  operate_seg(ms, x, -1)


@nb.njit
def ms_get(ms: np.ndarray, ms_len: int, i: int) -> int:
  assert 0 <= i < get_seg(ms, 0, ms_len)
  is_ok = lambda v, x: v < x
  return max_right_seg(ms, is_ok, i + 1, 0, ms_len)


@nb.njit
def ms_max(ms: np.ndarray, ms_len: int) -> int:
  return ms_get(ms, ms_len, ms_size(ms) - 1)


@nb.njit
def ms_min(ms: np.ndarray, ms_len: int) -> int:
  return ms_get(ms, ms_len, 0)


@nb.njit
def ms_lower_bound(ms: np.ndarray, x: int) -> int:
  return get_seg(ms, 0, x)


@nb.njit
def ms_upper_bound(ms: np.ndarray, x: int) -> int:
  return get_seg(ms, 0, x + 1)



@nb.njit((nb.i8[:], ), cache=True)
def solve(p: np.ndarray) -> typing.NoReturn:
  n = len(p)
  order = np.empty(n, np.int64)
  order[p] = np.arange(n)
  order = order[::-1]

  ms = ms_build(n)

  s = 0
  size = 0
  for i in order:
    k = ms_lower_bound(ms, i)
    l1 = ms_get(ms, n, k - 2) if k - 2 >= 0 else -1
    l0 = ms_get(ms, n, k - 1) if k - 1 >= 0 else -1
    r0 = ms_get(ms, n, k) if k < size else n
    r1 = ms_get(ms, n, k + 1) if k + 1 < size else n
    cnt = (l0 - l1) * (r0 - i) + (i - l0) * (r1 - r0)
    s += (p[i] + 1) * cnt
    ms_add(ms, i)
    size += 1
  print(s)


def main() -> typing.NoReturn:
  n = int(input())
  p = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  ) - 1
  solve(p)


main()
