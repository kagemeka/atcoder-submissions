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
  fw: np.ndarray,
  op: typing.Callable[[S, S], S],
  i: int,
  x: S,
) -> typing.NoReturn:
  i += 1
  while i < len(fw):
    fw[i] = op(fw[i], x)
    i += i & -i


@nb.njit
def fw_get(
  fw: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  i: int,
) -> typing.NoReturn:
  i += 1
  v = e()
  while i > 0:
    v = op(v, fw[i])
    i -= i & -i
  return v


@nb.njit
def fw_lower_bound(
  fw: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  search_fn: typing.Callable[[S], bool],
  k: S, # cuz it's impossible to use closure on numba(v0.53.1).
) -> int:
  n = len(fw)
  l = 1
  while l << 1 < n: l <<= 1
  v, i = e(), 0
  while l:
    if i + l < n and not search_fn(op(v, fw[i + l]), k):
      i += l
      v = op(v, fw[i])
    l >>= 1
  return i


@nb.njit
def fw_op(a: int, b: int) -> int:
  return a ^ b


@nb.njit
def fw_e() -> int:
  return 0


@nb.njit
def fw_inverse(a: int) -> int:
  return a


@nb.njit
def build_fw(a: np.ndarray) -> np.ndarray:
  return fw_build(fw_op, a)


@nb.njit
def set_point_fw(
  fw: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  fw_set(fw, fw_op, i, x)


@nb.njit
def get_half_range_fw(fw: np.ndarray, i: int) -> S:
  return fw_get(fw, fw_op, fw_e, i)


@nb.njit
def get_range_fw(fw: np.ndarray, l: int, r: int) -> S:
  return fw_op(
    fw_inverse(get_half_range_fw(fw, l - 1)),
    get_half_range_fw(fw, r - 1),
  )



@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(txy)
  fw = build_fw(a)
  for i in range(q):
    t, x, y = txy[i]
    if t == 1:
      set_point_fw(fw, x - 1, y)
    else:
      print(get_range_fw(fw, x - 1, y))



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
