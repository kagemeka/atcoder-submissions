import typing
import sys
import numpy as np

def solve(a: np.ndarray, t: int) -> typing.NoReturn:
  mn = np.minimum.accumulate(a)
  d = a - mn
  cnt = np.count_nonzero(d == d.max())
  print(cnt)


def main() -> typing.NoReturn:
  n, t = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, t)


main()
