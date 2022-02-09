import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def fw_build(
  n: int,
  e: int,
) -> np.ndarray:
  return np.full(n + 1, e, np.int64)


@nb.njit
def fw_build_from_array(
  a: np.ndarray,
  fn: typing.Callable[[int, int], int],
  e: int,
) -> np.ndarray:
  fw = a.copy()
  assert fw[0] == e
  n = fw.size
  for i in range(n):
    j = i + (i & -i)
    if j < n:
      fw[j] = fn(fw[j], fw[i])
  return fw


@nb.njit
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
  fn: typing.Callable[[int, int], int],
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] = fn(fw[i], x)
    i += i & -i


@nb.njit
def fw_get(
  fw: np.ndarray,
  i: int,
  fn: typing.Callable[[int, int], int],
  e: int,
) -> int:
  v = e
  while i > 0:
    v = fn(v, fw[i])
    i -= i & -i
  return v


@nb.njit
def fw_get_range(
  fw: np.ndarray,
  l: int,
  r: int,
  fn: typing.Callable[[int, int], int],
  e: int,
  inverse: typing.Callable[[int], int],
) -> int:
  lv = fw_get(fw, l - 1, fn, e)
  rv = fw_get(fw, r, fn, e)
  return fn(inverse(lv), rv)



@nb.njit(
  (nb.i8[:], nb.i8[:, :]),
  cache=True,
)
def solve(
  a: np.ndarray,
  txy: np.ndarray,
) -> typing.NoReturn:
  n, m = len(a), len(txy)
  fn = lambda x, y: x ^ y
  e = 0
  inv = lambda x: x
  fw = np.full(n + 1, e, np.int64)
  fw[1:] = a

  fw = fw_build_from_array(fw, fn, e)
  for j in range(m):
    t, x, y = txy[j]
    if t == 1:
      fw_set(fw, x, y, fn)
    else:
      print(fw_get_range(fw, x, y, fn, e, inv))


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
