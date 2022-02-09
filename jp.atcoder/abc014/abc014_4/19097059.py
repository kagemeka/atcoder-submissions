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


def read_int():
  return int(readline())



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


class Tree(Graph):
  def __init__(self, **kwargs):
    super(Tree, self).__init__(
      **kwargs)
    # self.init_root(**kwargs)


  def init_root(
      self,
      root: int=...,
      **kwargs
      ):
    inf = float('inf')
    n = len(self.nodes)
    valid = type(root) == int \
      and 0 <= root < n
    assert valid, 'Invalid root'
    self.root = root
    self.depth = [None] * n
    self.depth[root] = 0
    self.parent = [None] * n
    self.parent[root] = root
    self.dist = [inf] * n
    self.dist[root] = 0


  def _search(self, u):
    for v, e in \
        self.edges[u].items():
      if v == self.parent[u]:
        continue
      self.parent[v] = u
      self.depth[v] = \
        self.depth[u] + 1
      self.dist[v] = \
        self.dist[u] + e.weight
      self.que.append(v)


  def bfs(self, source: int=None):
    if source is not None:
      self.init_root(root=source)
    from collections import deque
    self.que = deque([self.root])
    while self.que:
      u = self.que.popleft()
      self._search(u)


class LowestCommonAncestor(Tree):
  def find_ancestors(self):
    # doubling
    self.ancestors = [self.parent]
    l = max(self.depth).bit_length()
    for _ in range(l):
      self.ancestors.append([
        self.ancestors[-1][u]
        for u in self.ancestors[-1]
      ])


  def find_dist(self, u, v):
    lca = self.find_lca(u, v)
    d = self.dist[u] \
      + self.dist[v] \
      - 2 * self.dist[lca]
    return d


  def _sort_by_depth(self, u, v):
    du = self.depth[u]
    dv = self.depth[v]
    if du > dv:
      u, v = v, u
    return u, v


  def _upstream(self, v, d):
    for i in range(d.bit_length()):
      if ~ d>>i & 1: continue
      v = self.ancestors[i][v]
    return v


  def find_lca(self, u, v):
    u, v = self._sort_by_depth(u, v)
    du = self.depth[u]
    dv = self.depth[v]
    v = self._upstream(v, dv - du)
    if v == u: return v

    l = du.bit_length()
    for i in range(l-1, -1, -1):
      nu = self.ancestors[i][u]
      nv = self.ancestors[i][v]
      if nu == nv: continue
      u, v = nu, nv
    lca = self.parent[u]

    return lca


def solve(n, xy, ab):
  g = LowestCommonAncestor(n=n)
  for x, y in xy:
    x -= 1; y -= 1
    g.add_edge(x, y, weight=1)
    g.add_edge(y, x, weight=1)

  g.bfs(source=0)
  g.find_ancestors()

  for a, b in ab:
    a -= 1; b -= 1
    print(g.find_dist(a, b) + 1)


def main():
  n = read_int()
  xy = [
    readline_ints()
    for _ in range(n-1)
  ]
  q = read_int()
  ab = [
    readline_ints()
    for _ in range(q)
  ]
  solve(n, xy, ab)


if __name__ == '__main__':
  main()
