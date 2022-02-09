import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.b1[:], ), cache=True)
def solve(c: np.ndarray) -> typing.NoReturn:
  n = len(c)

  a, b = np.sum(c == 1), 0
  res = max(a, b)
  for i in range(n):
    if c[i] == 1:
      a -= 1
    else:
      b += 1
    res = min(res, max(a, b))
  print(res)


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  c = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='S1',
  ) == b'R'
  solve(c)


main()
