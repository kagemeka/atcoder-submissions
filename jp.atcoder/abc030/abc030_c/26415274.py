import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8, nb.i8[:], nb.i8[:]), cache=True)
def solve(
  x: int,
  y: int,
  a: np.ndarray,
  b: np.ndarray,
) -> typing.NoReturn:
  n, m = len(a), len(b)
  t = 0
  cnt = 0
  i = j = 0
  while True:
    while i < n and a[i] < t: i += 1
    if i == n: break
    t = a[i] + x
    while j < m and b[j] < t: j += 1
    if j == m: break
    t = b[j] + y
    cnt += 1
  print(cnt)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  x, y = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  b = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(x, y, a, b)


main()
