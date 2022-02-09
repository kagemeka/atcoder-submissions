import typing
import sys
import numpy as np
import scipy
from scipy import sparse



def solve(
  n: np.ndarray,
  a: np.ndarray,
  b: np.ndarray,
  t: np.ndarray,
) -> typing.NoReturn:
  g = np.zeros(
    shape=(n, n),
    dtype=np.int64,
  )
  g[a, b] = t
  g += g.T
  dist = sparse.csgraph.shortest_path(
    csgraph=g,
    method='FW',
    directed=False,
  ).astype(np.int64)
  print(dist.max(axis=1).min())



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a, b, t = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3).T
  a -= 1
  b -= 1
  solve(n, a, b, t)


main()
