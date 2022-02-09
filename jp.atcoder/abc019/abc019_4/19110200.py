def read():
  import sys
  return sys.stdin.buffer.read()


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


def read_ints():
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )


def solve(n, m, p, q, xyz):
  import numpy as np
  from itertools import combinations
  x, y, z = np.transpose(xyz)
  x -= 1; y -= 1
  g = np.zeros(
    shape=(n, m),
    dtype=np.int32,
  )
  g[x, y] = z
  s = np.array([
    *combinations(range(n), p)
  ])
  mx_sat = np.sort(
    g[s].sum(axis=1),
    axis=1,
  )[:, -q:].sum(axis=1).max()
  print(mx_sat)


def main():
  n, m, p, q, r = readline_ints()
  xyz = read_ints().reshape(r, 3)
  solve(n, m, p, q, xyz)


if __name__ == '__main__':
  main()
