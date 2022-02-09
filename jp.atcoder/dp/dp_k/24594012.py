import typing
import sys
import numpy as np
import numba as nb


@nb.njit(
  (nb.i8, nb.i8[:]),
  cache=True,
)
def solve(
  k: int,
  a: np.array,
) -> typing.NoReturn:
  win = np.zeros(
    1 << 18,
    dtype=np.bool8,
  )
  for i in range(k):
    win[i + a] |= ~win[i]
  print(
    'First' if win[k]
    else 'Second',
  )


def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(k, a)


main()
