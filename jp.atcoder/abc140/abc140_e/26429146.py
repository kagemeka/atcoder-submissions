# binary search on Fenwick Tree
import typing
import sys
import numpy as np
import numba as nb



S = typing.TypeVar('S')
@nb.njit
def fw_build(
  op: typing.Callable[[S, S], S],
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  fw = np.empty((n + 1, ) + a.shape[1:], np.int64)
  fw[1:] = a.copy()
  for i in range(1, n + 1):
    j = i + (i & -i)
    if j < n + 1: fw[j] = op(fw[j], fw[i])
  return fw


@nb.njit
def fw_set(
  op: typing.Callable[[S, S], S],
  fw: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  assert 0 <= i < len(fw) - 1
  i += 1
  while i < len(fw):
    fw[i] = op(fw[i], x)
    i += i & -i


@nb.njit
def fw_get(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  fw: np.ndarray,
  i: int,
) -> S:
  assert 0 <= i < len(fw)
  v = e()
  while i > 0:
    v = op(v, fw[i])
    i -= i & -i
  return v


@nb.njit
def fw_max_right(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  fw: np.ndarray,
  is_ok: typing.Callable[[S], bool], # fn(v) -> bool
  x: S, # fn(v, x) cuz closure is not supported on nb v0.53.1.
) -> int:
  n = len(fw)
  l = 1
  while l << 1 < n: l <<= 1
  v, i = e(), 0
  while l:
    if i + l < n and is_ok(op(v, fw[i + l]), x):
      i += l
      v = op(v, fw[i])
    l >>= 1
  return i


S = typing.TypeVar('S')
@nb.njit
def build_fw(a: np.ndarray) -> np.ndarray:
  return fw_build(fw_op, a)


@nb.njit
def set_fw(fw: np.ndarray, i: int, x: S) -> typing.NoReturn:
  fw_set(fw_op, fw, i, x)


@nb.njit
def get_fw(fw: np.ndarray, i: int) -> S:
  return fw_get(fw_op, fw_e, fw, i)


@nb.njit
def get_range_fw(fw: np.ndarray, l: int, r: int) -> S:
  return fw_op(
    fw_inverse(fw_get(fw_op, fw_e, fw, l)),
    fw_get(fw_op, fw_e, fw, r),
  )


@nb.njit
def max_right_fw(
  fw: np.ndarray,
  is_ok: typing.Callable[[S], bool], # fn(v) -> bool
  x: S,
) -> int:
  return fw_max_right(fw_op, fw_e, fw, is_ok, x)

@nb.njit
def fw_op(a: S, b: S) -> S: return a + b

@nb.njit
def fw_e() -> S: return 0

@nb.njit
def fw_inverse(a: S) -> S: return -a


@nb.njit((nb.i8[:], ), cache=True)
def solve(p: np.ndarray) -> typing.NoReturn:
  n = len(p)
  order = np.empty(n, np.int64)
  order[p] = np.arange(n)
  order = order[::-1]

  is_ok = lambda v, x: v < x
  fw = build_fw(np.zeros(n, np.int64))

  s = 0
  for i in order:
    k = get_fw(fw, i)
    l1 = max_right_fw(fw, is_ok, k - 1) if k >= 2 else -1
    l0 = max_right_fw(fw, is_ok, k) if k >= 1 else -1
    r0 = max_right_fw(fw, is_ok, k + 1)
    r1 = max_right_fw(fw, is_ok, k + 2)
    cnt = (l0 - l1) * (r0 - i) + (i - l0) * (r1 - r0)
    s += (p[i] + 1) * cnt
    set_fw(fw, i, 1)
  print(s)


def main() -> typing.NoReturn:
  n = int(input())
  p = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  ) - 1
  solve(p)


main()
