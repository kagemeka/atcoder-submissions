import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8, ),
  cache=True,
)
def fw_build(n: int) -> np.ndarray:
  return np.full(n + 1, 0, np.int64)


@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def fw_build_from_array(
  a: np.ndarray,
) -> np.ndarray:
  fw = a.copy()
  assert a[0] == 0
  n = fw.size
  for i in range(n):
    j = i + (i & -i)
    if j < n: fw[j] ^= fw[i]
  return fw


@nb.njit(
  (nb.i8[:], nb.i8, nb.i8),
  cache=True,
)
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] ^= x
    i += i & -i


@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def fw_get(
  fw: np.ndarray,
  i: int,
) -> int:
  v = 0
  while i > 0:
    v ^= fw[i]
    i -= i & -i
  return v


@nb.njit(
  (nb.i8[:], nb.i8, nb.i8),
  cache=True,
)
def fw_get_range(
  fw: np.ndarray,
  l: int,
  r: int,
) -> int:
  return fw_get(fw, l - 1) ^ fw_get(fw, r)



@nb.njit(
  (nb.i8[:], nb.i8[:, :]),
  cache=True,
)
def solve(
  a: np.ndarray,
  txy: np.ndarray,
) -> typing.NoReturn:
  n, m = len(a), len(txy)
  fw = np.zeros(n + 1, np.int64)
  fw[1:] = a
  fw = fw_build_from_array(fw)
  for j in range(m):
    t, x, y = txy[j]
    if t == 1:
      fw_set(fw, x, y)
    else:
      print(fw_get_range(fw, x, y))



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
