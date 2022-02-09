def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def readline_ints():
  import numpy as np
  return np.fromstring(
    string=readline().decode(),
    dtype=np.int64,
    sep=' ',
  )


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


def solve(n, p, ab):
  import networkx as nx
  g = nx.DiGraph()
  g.add_nodes_from(range(n+1))
  g.add_edges_from(ab, capacity=1)
  g.add_edges_from(
    ab[:, ::-1], capacity=1)
  g.add_edges_from(
    zip(p, [n]*len(p)),
    capacity=1,
  )
  min_cut = nx.minimum_cut_value(
    flowG=g,
    _s=0, _t=n,
  )
  print(min_cut)


def main():
  import numpy as np
  n, _, _ = readline_ints()
  p = readline_ints()
  ab = read_ints().reshape(-1, 2)
  solve(n, p, ab)


if __name__ == '__main__':
  main()
