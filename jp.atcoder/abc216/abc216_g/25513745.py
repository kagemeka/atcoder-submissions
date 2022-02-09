import typing


class Node(): ...



class Edge():
  def __init__(
    self,
    from_: int,
    to: int,
    weight: typing.Optional[int] = None,
    capacity: typing.Optional[int] = None,
  ) -> typing.NoReturn:
    self.from_ = from_
    self.to = to
    self.weight = weight
    self.capacity = capacity




class Graph():
  def __init__(
    self,
    nodes: typing.List[Node],
    edges: typing.List[typing.List[Edge]],
  ) -> typing.NoReturn:
    self.nodes = nodes
    self.edges = edges


  @classmethod
  def from_size(
    cls,
    n: int,
  ) -> typing.Any:
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




class Config():
  def __init__(
    self,
    inf: int = 1 << 60,
  ) -> typing.NoReturn:
    self.inf = inf



class ShortestDistDijkstra():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    import heapq
    n = g.size
    dist = [self.__cfg.inf] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
      du, u = heapq.heappop(hq)
      if du > dist[u]: continue
      for e in g.edges[u]:
        v, dv = e.to, du + e.weight
        if dv >= dist[v]: continue
        dist[v] = dv
        heapq.heappush(hq, (dv, v))
    return dist


  def __init__(
    self,
    cfg: Config,
  ) -> typing.NoReturn:
    self.__cfg = cfg



import sys

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrx = map(
    int,
    sys.stdin.read().split(),
  )
  lrx = zip(*[lrx] * 3)
  solve(n, lrx)


def solve(
  n: int,
  lrx: typing.Iterator[
    typing.Tuple[int],
  ],
) -> typing.NoReturn:
  g = Graph.from_size(n + 1)
  for l, r, x in lrx:
    e = Edge(l - 1, r, r - l + 1 - x)
    g.add_edge(e)
  for i in range(n):
    g.add_edge(Edge(i, i + 1, 1))
    g.add_edge(Edge(i + 1, i, 0))
  dijkstra = ShortestDistDijkstra(
    Config(inf=1 << 60),
  )
  b = dijkstra(g, 0)
  a = [(b[i + 1] - b[i]) ^ 1 for i in range(n)]
  print(*a)


main()
