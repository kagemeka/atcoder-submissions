import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.b1[:], ), cache=True)
def solve(c: np.ndarray) -> typing.NoReturn:
  n = len(c)
  a = np.sort(c)[::-1]
  s = 0
  for i in range(n):
    s += a[i] != c[i]
  print(s // 2)


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  c = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='S1',
  ) == b'R'
  solve(c)


main()
