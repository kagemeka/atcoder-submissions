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


class Edge:
  def __init__(
      self,
      weight=1,
      capacity=1,
      **kwargs,
      ):
    self.weight = weight
    self.capacity = capacity

  def __str__(self):
    s = f'weight: {self.weight},' \
      f' cap: {self.capacity}'
    return s

class Node:
  def __init__(self, **kwargs):
    pass

class Graph:
  def __init__(self, n=0):
    self.__N = n
    self.nodes = [None] * n
    self.edges = [
      {} for _ in range(n)]

  def add_node_info(
      self,
      v,
      **kwargs):
    self.nodes[v] = Node(**kwargs)

  def add_edge(
      self,
      u, v,
      update=False,
      **kwargs):
    if not update and \
        v in self.edges[u]:
      return
    self.edges[u][v] = Edge(
      **kwargs)



from abc import abstractmethod

class ShortestPath(Graph):
  @abstractmethod
  def shortest_dist(self, **kwargs):
    ...


class FloydWarshall(ShortestPath):
  def make_dist_matrix(self):
    n = len(self.nodes)
    inf = float('inf')
    d = [[inf]*n for _ in range(n)]
    for u in range(n):
      d[u][u] = 0
      for v, e in \
          self.edges[u].items():
        d[u][v] = e.weight
    return d


  def shortest_dist(self):
    d = self.make_dist_matrix()
    n = len(d)
    for w in range(n):
      for u in range(n):
        for v in range(n):
          d[u][v] = min(
            d[u][v],
            d[u][w] + d[w][v],
          )
    return d


def solve(n, abt):
  g = FloydWarshall(n=n)
  for a, b, t in abt:
    a -= 1; b -= 1
    g.add_edge(a, b, weight=t)
    g.add_edge(b, a, weight=t)

  res = min(
    max(d)
    for d in g.shortest_dist()
  )
  print(res)


def main():
  n, m = readline_ints()
  abt = read_ints()
  abt = zip(*[iter(abt)]*3)
  solve(n, abt)


if __name__ == '__main__':
  main()
