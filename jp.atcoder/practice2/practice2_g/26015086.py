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
  label = label.tolist()
  scc = [[] for _ in range(k)]
  for i, l in enumerate(label):
    scc[l].append(i)
  print(k)
  for s in scc[::-1]:
    print(len(s), *s)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2)
  solve(n, ab)


main()
