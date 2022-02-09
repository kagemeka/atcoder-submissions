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
    self.inf = float('inf')


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



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    r = reader.int()
    c = reader.int()
    sy = reader.int() - 1
    sx = reader.int() - 1
    gy = reader.int() - 1
    gx = reader.int() - 1

    maze = [None] * r
    for i in range(r):
      maze[i] = reader.str()
    maze = ''.join(maze)

    self.r = r
    self.c = c
    self.sy = sy
    self.sx = sx
    self.gy = gy
    self.gx = gx
    self.maze = maze


  def solve(self):
    c = self.c
    self.moves = (-c, -1, 1, c)
    self.make_graph()
    print(self.calc_dist())


  def calc_dist(self) -> int:
    g = self.g
    c = self.c
    src = self.sy * c + self.sx
    dst = self.gy * c + self.gx
    bfs = GraphBFS(graph=g)
    bfs.search(src)
    dist = bfs.level[dst]
    return dist


  def make_graph(
    self,
  ):
    r, c = self.r, self.c
    n = r * c
    g = Graph(n)
    for i in range(n):
      edges = self.gen_edges(i)
      g.add_edges(edges)
    self.g = g


  def gen_edges(
    self,
    i: int,
  ):
    edges = []
    maze = self.maze
    if maze[i] == '#':
      return edges
    for d in self.moves:
      j = i + d
      if maze[j] == '#':
        continue
      e = Edge(
        from_ = i,
        to = j,
      )
      edges.append(e)
    return edges



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
