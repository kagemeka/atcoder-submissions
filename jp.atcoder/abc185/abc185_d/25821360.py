import typing
import sys
import numpy as np


def solve(
  n: int,
  a: np.ndarray,
) -> typing.NoReturn:
  a = np.pad(a, pad_width=1, constant_values=(0, n + 1))
  a.sort()
  d = a[1:] - a[:-1] - 1
  if np.count_nonzero(d) == 0:
    print(0)
    return
  k = d[d > 0].min()
  cnt = (d + k - 1) // k
  print(cnt.sum())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(n, a)


main()
