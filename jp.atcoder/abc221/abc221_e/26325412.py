import typing
import sys
import numpy as np
import numba as nb

MOD = 998_244_353


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
  seg: np.ndarray,
  op: np.ndarray,
  e: np.ndarray,
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
def seg_op(a: S, b: S) -> S: return (a + b) % MOD


@nb.njit
def seg_e() -> S: return 0



@nb.njit
def mod_pow2_inverse(n: int, p: int) -> np.ndarray:
  inv_2 = (p + 1) // 2
  a = np.ones(n, np.int64)
  for i in range(n - 1): a[i + 1] = a[i] * inv_2 % p
  return a


@nb.njit
def mod_pow2(n: int, p: int) -> np.ndarray:
  a = np.ones(n, np.int64)
  for i in range(n - 1): a[i + 1] = a[i] * 2 % p
  return a


@nb.njit
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 2]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  m = 1 << 20
  MOD = 998_244_353
  pow2 = mod_pow2(m, MOD)
  pow2_inv = mod_pow2_inverse(m, MOD)
  a, _ = compress_array(a)
  seg = build_seg(np.zeros(m, np.int64))
  cnt = 0
  for i in range(n):
    x = a[i]
    cnt += get_seg(seg, 0, x + 1) * pow2[i - 1] % MOD
    set_seg(seg, x, pow2_inv[i])
  print(cnt % MOD)




def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
