import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def set_val(
  a: np.array,
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < a.size:
    a[i] = max(a[i], x)
    i += i & -i


@nb.njit
def get_mx(
  a: np.array,
  i: int,
) -> int:
  mx = 0
  while i > 0:
    mx = max(mx, a[i])
    i -= i & -i
  return mx



@nb.njit(
  (nb.i8, nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  n: int,
  h: np.array,
  a: np.array,
) -> typing.NoReturn:
  idx = np.argsort(h)
  # a = a[i]
  seg = np.zeros(
    n + 1,
    dtype=np.int64,
  )
  mx = 0
  for i in idx:
    v = get_mx(seg, i) + a[i]
    mx = max(mx, v)
    set_val(seg, i + 1, v)
  print(mx)




def main() -> typing.NoReturn:
  n = int(input())
  h = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, h, a)


main()
