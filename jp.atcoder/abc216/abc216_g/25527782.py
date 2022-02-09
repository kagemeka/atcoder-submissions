import typing
import sys
import numpy as np
import numba as nb



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
def fw_build(
  n: int,
  e: int,
) -> np.ndarray:
  fw = np.full(n + 1, e, np.int64)
  return fw


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  lrx: np.ndarray,
) -> typing.NoReturn:
  e = 0
  fn = lambda x, y: x + y
  fw = fw_build(1 << 18, e)
  sort_idx = np.argsort(lrx[:, 1], kind='mergesort')
  lrx = lrx[sort_idx]
  a = np.zeros(n, np.int64)
  i = 0
  st = []
  for k in range(len(lrx)):
    l, r, x = lrx[k]
    while i < r:
      st.append(i)
      i += 1
    c = fw_get(fw, r, fn, e) - fw_get(fw, l - 1, fn,e)
    for _ in range(x - c):
      j = st.pop()
      fw_set(fw, j + 1, 1, fn)
      a[j] = 1
  return a


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrx = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  a = solve(n, lrx)
  print(*a)


main()
