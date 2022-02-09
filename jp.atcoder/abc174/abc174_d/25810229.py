import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.b1[:], ), cache=True)
def solve(c: np.ndarray) -> typing.NoReturn:
  n = len(c)
  idx = np.arange(n)
  w = idx[~c]
  r = idx[c][::-1]
  cnt = 0
  for i in range(n):
    if i >= len(w) or i >= len(r): break
    if w[i] > r[i]: break
  print(i)




def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  c = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='S1',
  ) == b'R'
  solve(c)


main()
