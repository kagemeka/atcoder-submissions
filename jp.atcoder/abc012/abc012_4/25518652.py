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
  g = sparse.csr_matrix(
    (t, (a, b)),
    shape=(n, n),
    dtype=np.int64,
  )
  dist = sparse.csgraph.floyd_warshall(
    g,
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
