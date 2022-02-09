import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(s: np.ndarray, t: np.ndarray) -> typing.NoReturn:
  si = np.flatnonzero(s == 0)
  ti = np.flatnonzero(t == 0)
  if si.size != ti.size:
    print(-1)
    return
  print(np.sum(si != ti))


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='S1',
  ).astype(np.int64)
  t = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='S1',
  ).astype(np.int64)
  solve(s, t)


main()
