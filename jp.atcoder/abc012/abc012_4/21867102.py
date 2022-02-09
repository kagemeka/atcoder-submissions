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



# import numpy as np


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



class FloydWarshall:


  def __init__(
    self,
    graph: Graph,
  ):
    self.g = graph
    self.inf = float('inf')


  def __call__(
    self,
  ) -> None:
    self.init_dist_mat()
    n = self.g.size
    for i in range(n):
      self.mid = i
      self.support0()


  def support0(self):
    n = self.g.size
    for i in range(n):
      self.src = i
      self.support1()


  def support1(self):
    n = self.g.size
    dist = self.dist
    k, i = self.mid, self.src
    for j in range(n):
      d = min(
        dist[i][j],
        dist[i][k] + dist[k][j]
      )
      dist[i][j] = d


  def init_dist_mat(
    self,
  ):
    n = self.g.size
    dist = [
      [self.inf] * n
      for _ in range(n)
    ]
    self.dist = dist
    for i in range(n):
      self.i = i
      self.__init_dist()


  def __init_dist(
    self,
  ):
    dist = self.dist
    i = self.i
    dist[i][i] = 0
    g = self.g
    for e in g.edges[i]:
      j = e.to
      dist[i][j] = e.weight



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    n = reader.int()
    m = reader.int()
    a = [
      reader.int()
      for _ in range(3 * m)
    ]
    a = np.array(
      a,
    ).reshape(m, 3)
    a[:, :2] -= 1
    self.n, self.m = n, m
    self.a = a


  def solve(self):
    self.make_graph()
    self.compute_dist_mat()
    dist = self.dist
    d = min(
      max(d)
      for d in dist
    )
    print(d)


  def compute_dist_mat(
    self,
  ):
    fw = FloydWarshall(self.g)
    fw()
    self.dist = fw.dist


  def make_graph(
    self,
  ):
    a = self.a
    n = self.n
    g = Graph(n)
    for i, j, w in a:
      e = Edge(
        from_=i,
        to=j,
        weight=w,
      )
      g.add_edge(e)
      e = Edge(
        from_=j,
        to=i,
        weight=w,
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
