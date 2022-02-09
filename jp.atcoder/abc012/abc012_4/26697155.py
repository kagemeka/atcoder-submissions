import typing
import sys
import numpy as np
from scipy import sparse


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a, b, t = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(m, 3).T
  g = sparse.csr_matrix((t, (a - 1, b - 1)), shape=(n, n), dtype=np.int64)
  dist = sparse.csgraph.floyd_warshall(g, directed=False).astype(np.int64)
  print(dist.max(axis=1).min())


main()
