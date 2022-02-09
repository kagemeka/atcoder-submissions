import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] += x
    i += i & -i

@nb.njit
def fw_get(
  fw: np.ndarray,
  i: int,
) -> int:
  v = 0
  while i > 0:
    v += fw[i]
    i -= i & -i
  return v


@nb.njit((nb.i8, nb.i8, nb.i8[:, :]), cache=True)
def solve(
  h: int,
  w: int,
  yx: np.ndarray,
) -> typing.NoReturn:
  m = len(yx)
  min_y = np.full(w, h, np.int64)
  min_x = np.full(h, w, np.int64)

  for i in range(m):
    y, x = yx[i]
    min_y[x] = min(min_y[x], y)
    min_x[y] = min(min_x[y], x)

  cnt = 0
  cnt += min_y[:min_x[0]].sum()
  cnt += min_x[:min_y[0]].sum()

  fw = np.zeros(w + 1, np.int64)
  for i in range(min_x[0]):
    fw_set(fw, i + 1, 1)

  sorted_x = np.argsort(min_y)
  sorted_y = min_y[sorted_x]
  k = 0
  for i in range(min_y[0]):
    while k < w and sorted_y[k] <= i:
      x = sorted_x[k]
      if x < min_x[0]:
        fw_set(fw, x + 1, -1)
      k += 1
    cnt -= fw_get(fw, min_x[i])

  print(cnt)




def main() -> typing.NoReturn:
  h, w, m = map(int, input().split())
  yx = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(h, w, yx)


main()
