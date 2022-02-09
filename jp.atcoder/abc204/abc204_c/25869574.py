import typing
import sys
import numpy as np
import scipy.sparse



def solve(n: int, ab: np.ndarray) -> typing.NoReturn:
  a, b = ab.T
  c = np.full(len(a), 1, np.int64)
  g = scipy.sparse.csr_matrix(
    (c, (a, b)),
    shape=(n, n),
    dtype=np.int64,
  )
  cnt = 0
  for i in range(n):
    t = scipy.sparse.csgraph.depth_first_tree(
      csgraph=g,
      i_start=i,
      directed=True,
    ).astype(np.int64)
    cnt += t.size + 1
  print(cnt)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, ab)


main()
