import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8, nb.i8), cache=True)
def solve(a: np.ndarray, s: int, t: int) -> typing.NoReturn:
  n = len(a)
  for i in range(n - 1):
    a[i + 1] += a[i]

  cnt = 0
  for x in a:
    cnt += s <= x <= t
  print(cnt)


def main() -> typing.NoReturn:
  n, s, t = map(int, input().split())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a, s, t)

main()
