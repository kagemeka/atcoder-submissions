def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def read():
  import sys
  return sys.stdin.buffer.read()


def read_ints():
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )


def solve(n, a, b, t):
  from scipy.sparse.csgraph import (
    floyd_warshall,
  )
  from scipy.sparse import (
    csr_matrix,
  )
  import numpy as np
  g = csr_matrix(
    arg1=(t, (a, b)),
    shape=(n, n),
  )
  res = floyd_warshall(
    csgraph=g,
    directed=False,
  ).max(axis=1).min()
  print(res.astype(np.int64))


def main():
  import numpy as np
  n, m = readline_ints()
  abt = read_ints().reshape(m, 3)
  a, b, t = np.transpose(abt)
  a -= 1; b -= 1
  solve(n, a, b, t)


if __name__ == '__main__':
  main()
