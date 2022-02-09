import typing
import numpy as np
import sys


def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  s = np.pad(a, (1, 0))
  s = s.cumsum()
  dpl = np.zeros(
    (n, n),
    dtype=np.int64,
  )
  dpr = np.zeros(
    (n, n),
    dtype=np.int64,
  )
  for i in range(1, n):
    x = np.min(
      dpl[:-i, :i]
      + dpr[i:, i - 1::-1],
      axis=1,
    )
    x += s[i+1:] - s[:-i-1]
    dpl[: -i, i] = x
    dpr[i:, i] = x

  print(dpl[0, -1])


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


main()
