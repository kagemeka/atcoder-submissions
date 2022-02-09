import typing
import sys
import numpy as np


# @nb.njit((nb.i8[:, :], nb.i8[:]), cache=True)
def solve(d: np.ndarray, p: np.ndarray) -> typing.NoReturn:
  n = len(d)
  q = len(p)
  d = np.pad(d, pad_width=1)
  d = d.cumsum(axis=0).cumsum(axis=1)

  res = np.zeros(n * n + 1, np.int64)
  for dy in range(1, n + 1):
    for dx in range(1, n + 1):
      k = dx * dy
      mx = np.max(
        d[dy:, dx:]
        - d[dy:, :-dx]
        - d[:-dy, dx:]
        + d[:-dy, :-dx]
      )
      res[k] = max(res[k], mx)
  np.maximum.accumulate(res, out=res)
  print(*res[p], sep='\n')



def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  d = I[:n * n].reshape(n, n)
  p = I[n * n + 1:]
  solve(d, p)


main()
