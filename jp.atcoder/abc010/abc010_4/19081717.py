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
  *ints, = map(
    int,
    read().split(),
  )
  return ints


def solve(n, p, ab):
  x, y = [], []
  for a, b in ab:
    x.append(a)
    y.append(b)
    x.append(b)
    y.append(a)
  for a in p:
    x.append(a)
    y.append(n)

  if not x:
    print(0)
    return

  from scipy.sparse.csgraph import (
    maximum_flow,
  )
  from scipy.sparse import (
    csr_matrix,
  )
  g = csr_matrix(
    arg1=([1] * len(x), (x, y)),
    shape=(n+1, n+1),
  )
  min_cut = maximum_flow(
    csgraph=g,
    source=0,
    sink=n,
  ).flow_value
  print(min_cut)


def main():
  n, _, _ = readline_ints()
  p = readline_ints()
  ab = read_ints()
  ab = zip(*[iter(ab)]*2)
  solve(n, p, ab)


if __name__ == '__main__':
  main()
