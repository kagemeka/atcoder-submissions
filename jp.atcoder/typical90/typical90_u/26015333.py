import typing
import sys
import numpy as np
import scipy.sparse


def solve(n: int, ab: np.ndarray) -> typing.NoReturn:
  a, b = ab.T
  m = a.size
  c = np.full(m, 1, np.int64)
  g = scipy.sparse.csr_matrix(
    (c, (a, b)),
    shape=(n, n),
    dtype=np.int64,
  )
  k, label = scipy.sparse.csgraph.connected_components(
    csgraph=g,
    directed=True,
    connection='strong',
    return_labels=True,
  )
  b = np.bincount(label)
  cnt = np.sum(b * (b - 1) // 2)
  print(cnt)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, ab)


main()
