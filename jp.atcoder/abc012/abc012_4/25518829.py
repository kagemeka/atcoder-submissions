from __future__ import annotations
import typing
import dataclasses


@dataclasses.dataclass
class Node(): ...



@dataclasses.dataclass
class Edge():
  from_: int
  to: int
  weight: typing.Optional[int] = None,
  capacity: typing.Optional[int] = None



@dataclasses.dataclass
class Graph():
  nodes: typing.List[Node]
  edges: typing.List[typing.List[Edge]]

  @classmethod
  def from_size(
    cls,
    n: int,
  ) -> Graph:
    nodes = [Node() for _ in range(n)]
    edges = [[] for _ in range(n)]
    return cls(nodes, edges)


  def add_edge(
    self,
    e: Edge,
  ) -> typing.NoReturn:
    self.edges[e.from_].append(e)


  def add_edges(
    self,
    edges: typing.List[Edge],
  ) -> typing.NoReturn:
    for e in edges:
      self.add_edge(e)


  @property
  def size(self) -> int:
    return len(self.nodes)



@dataclasses.dataclass
class Config():
  inf: int = 1 << 60



class FloydWarshall():
  def __call__(
    self,
    g: Graph,
  ) -> typing.List[typing.List[int]]:
    n = g.size
    dist = [[self.__cfg.inf] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u in range(n):
      for e in g.edges[u]:
        dist[u][e.to] = min(dist[u][e.to], e.weight)

    for k in range(n):
      for i in range(n):
        for j in range(n):
          dist[i][j] = min(
            dist[i][j],
            dist[i][k] + dist[k][j],
          )
    return dist


  def __init__(
    self,
    cfg: Config,
  ) -> typing.NoReturn:
    self.__cfg = cfg




def solve(
  n: int,
  abt: typing.Iterator[
    typing.Tuple[int],
  ],
) -> typing.NoReturn:
  g = Graph.from_size(n)
  for a, b, t in abt:
    a -= 1; b -= 1
    g.add_edge(Edge(a, b, t))
    g.add_edge(Edge(b, a, t))

  fw = FloydWarshall(Config(inf=1 << 60))
  dist = fw(g)
  print(min(max(x) for x in dist))


import sys

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abt = map(int, sys.stdin.read().split())
  abt = zip(*[abt] * 3)
  solve(n, abt)


main()
