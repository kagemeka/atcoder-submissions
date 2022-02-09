from __future__ import (
  annotations,
)

from typing import (
  Generator,
  NoReturn
)


class StdReader:


  def __init__(
    self,
  ) -> NoReturn:
    import sys
    self.buf = sys.stdin.buffer
    self.lines = (
      self.async_readlines()
    )
    self.chunks: Generator


  def async_readlines(
    self,
  ) -> Generator:
    while True:
      gen = self.line_chunks()
      yield gen


  def line_chunks(
    self,
  ) -> Generator:
    ln = self.buf.readline()
    for chunk in ln.split():
      yield chunk


  def __call__(
    self,
  ) -> bytes:
    try:
      chunk = next(self.chunks)
    except:
      self.chunks = next(
        self.lines,
      )
      chunk = self()
    return chunk


  def str(
    self,
  ) -> str:
    b = self()
    return b.decode()


  def int(
    self,
  ) -> int:
    return int(self.str())



from abc import (
  ABC,
  abstractmethod,
)


class Solver(ABC):


  def __init__(self):
    self.reader = StdReader()


  def __call__(
    self,
  ):
    self.prepare()
    self.solve()


  @abstractmethod
  def prepare(self):
    ...


  @abstractmethod
  def solve(self):
    ...



import numpy as np


from typing import (
  List,
)


from dataclasses import (
  dataclass,
)



@dataclass
class Node:
  id_: int = None



@dataclass
class Edge:
  id_: int = None
  from_ : int = ...
  to: int = ...
  weight: int = 1
  capacity: int = 0



@dataclass
class Graph:


  nodes: List[Node]
  edges: List[List[Edge]]


  def __init__(
    self,
    n: int,
  ):
    nodes = [
      Node(i)
      for i in range(n)
    ]
    edges = [
      [] for _ in range(n)
    ]
    self.nodes = nodes
    self.edges = edges


  def add_edge(
    self,
    e: Edge,
  ):
    i = e.from_
    self.edges[i].append(e)


  def add_edges(
    self,
    edges: List[Edge],
  ):
    for e in edges:
      self.add_edge(e)


  @property
  def size(self):
    return len(self.nodes)



from typing import (
  List,
)



from collections import (
  deque,
)

class GraphBFS:


  level: List[int]


  def __init__(
    self,
    graph: Graph,
  ):
    self.g = graph


  def search(
    self,
    src: int,
  ):
    self.init_level()
    self.level[src] = 0
    self.set_queue()
    que = self.queue
    que.append(src)
    while que:
      x = que.popleft()
      self.explore(x)


  def explore(
    self,
    u: int,
  ):
    g = self.g
    lv = self.level
    que = self.queue
    for e in g.edges[u]:
      v = e.to
      if lv[v] is not None:
        continue
      lv[v] = lv[u] + 1
      que.append(v)


  def set_queue(self):
    que = deque()
    self.queue = que


  def init_level(self):
    lv = [None] * self.g.size
    self.level = lv



class Tree(Graph):
  ...



class TreeBFS:

  root: int
  depth: int
  dist: int
  parent: List[int]


  def __init__(
    self,
    tree: Tree,
  ):
    self.g = tree
    self.inf = float('inf')


  def search(
    self,
    root: int,
  ):
    self.src = root
    self.init_parent()
    self.init_depth()
    self.init_dist()
    self.set_queue()
    que = self.queue
    que.append(root)
    while que:
      x = que.popleft()
      self.explore(x)


  def explore(
    self,
    u: int,
  ):
    g = self.g
    dep = self.depth
    dist = self.dist
    par = self.parent
    que = self.queue
    for e in g.edges[u]:
      v = e.to
      if dep[v] is not None:
        continue
      d = e.weight
      dep[v] = dep[u] + 1
      dist[v] = dist[u] + d
      par[v] = u
      que.append(v)


  def set_queue(self):
    que = deque()
    self.queue = que


  def init_depth(self):
    dep = [None] * self.g.size
    dep[self.src] = 0
    self.depth = dep


  def init_parent(self):
    par = [None] * self.g.size
    par[self.src] = self.src
    self.parent = par


  def init_dist(self):
    inf = self.inf
    dist = [inf] * self.g.size
    dist[self.src] = 0
    self.dist = dist



class LCA:


  def __init__(
    self,
    tree: Tree,
  ):
    self.g = tree
    self.preprocess()


  def calc_dist(
    self,
    u: int,
    v: int,
  ) -> int:
    lca = self.find_lca(u, v)
    dist = self.dist
    du, dv = dist[u], dist[v]
    d_lca = dist[lca]
    return du + dv - 2 * d_lca


  def preprocess(
    self,
  ):
    bfs = TreeBFS(self.g)
    bfs.search(0)
    self.parent = bfs.parent
    self.depth = bfs.depth
    self.dist = bfs.dist
    self.find_ancestors()


  def find_ancestors(
    self,
  ):
    n = self.g.size
    dep = self.depth
    m = max(dep).bit_length()
    ancestors = np.zeros(
      (m, n),
      dtype=int,
    )
    ancestors[0] = np.array(
      self.parent,
    )
    for i in range(m - 1):
      a = ancestors[i]
      ancestors[i + 1] = a[a]
    ancestors = list(ancestors)
    for i in range(m):
      a = list(ancestors[i])
      ancestors[i] = a
    self.ancestors = ancestors


  def find_lca(
    self,
    u: int,
    v: int,
  ) -> int:
    u, v = self.sort(u, v)
    dep = self.depth
    du, dv = dep[u], dep[v]
    v = self.upstream(
      v,
      dv - du,
    )
    if v == u:
      return u
    return self._find_support(
      du, u, v,
    )


  def _find_support(
    self,
    dep: int,
    u: int,
    v: int,
  ) -> int:
    n = dep.bit_length()
    ancestors = self.ancestors
    for i in range(
      n - 1, -1, -1,
    ):
      a = ancestors[i]
      nu, nv = a[u], a[v]
      if nu == nv:
        continue
      u, v = nu, nv
    return self.parent[u]


  def upstream(
    self,
    v: int,
    d: int,
  ):
    n = d.bit_length()
    for i in range(n):
      if ~d >> i & 1:
        continue
      v = self.ancestors[i][v]
    return v


  def sort(
    self,
    u: int,
    v: int,
  ):
    dep = self.depth
    du, dv = dep[u], dep[v]
    if du > dv:
      u, v = v, u
    return u, v



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    n = reader.int()
    a = [
      reader.int()
      for _ in range(
        2 * (n - 1),
      )
    ]
    a = np.array(
      a,
    ).reshape(n - 1, 2) - 1
    self.n = n
    self.a = a


  def solve(self):
    self.make_graph()
    self.lca = LCA(self.g)
    reader = self.reader
    n = reader.int()
    for _ in range(n):
      a = reader.int() - 1
      b = reader.int() - 1
      self.query(a, b)


  def query(
    self,
    u: int,
    v: int,
  ):
    lca = self.lca
    d = lca.calc_dist(u, v)
    print(d + 1)


  def make_graph(
    self,
  ):
    n = self.n
    g = Tree(n)
    a = self.a
    for x, y in a:
      e = Edge(
        from_ = x,
        to = y,
      )
      g.add_edge(e)
      e = Edge(
        from_ = y,
        to = x,
      )
      g.add_edge(e)
    self.g = g



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
