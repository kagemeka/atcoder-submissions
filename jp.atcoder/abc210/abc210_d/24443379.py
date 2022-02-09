import sys
import numpy as np
import typing
import numba as nb


@nb.njit
def calc_min(
  a: np.array,
  c: int,
) -> int:
  h, w = a.shape
  mn = 1 << 40
  a = a.copy()
  for j in range(w - 1):
    x = a[0, j] + c
    mn = min(
      mn,
      x + a[0, j + 1],
    )
    a[0, j + 1] = min(
      a[0, j + 1],
      x,
    )
  for i in range(h - 1):
    x = a[i, 0] + c
    mn = min(
      mn,
      x + a[i + 1, 0],
    )
    a[i + 1, 0] = min(
      a[i + 1, 0],
      x,
    )
  for i in range(1, h):
    for j in range(1, w):
      x = min(
        a[i - 1, j],
        a[i, j - 1],
      ) + c
      mn = min(mn, x + a[i, j])
      a[i, j] = min(a[i, j], x)

  return mn


@nb.njit
def solve(
  a: np.array,
  c: int,
) -> typing.NoReturn:
  mn = min(
    calc_min(a, c),
    calc_min(a[::-1], c),
  )
  print(mn)



def main() -> typing.NoReturn:
  h, w, c = map(
    int,
    input().split(),
  )
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(h, w)
  solve(a, c)


main()
