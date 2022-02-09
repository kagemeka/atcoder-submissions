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


from abc import (
  ABCMeta,
  abstractmethod,
)


class Edge:
  def __init__(
      self,
      weight=1,
      capacity=1,
      **args,
      ):
    self.weight = weight
    self.capacity = capacity

  def __str__(self):
    s = f'weight: {self.weight},' \
      f' cap: {self.capacity}'
    return s

class Node:
  def __init__(self, **args):
    pass


class Graph:
  def __init__(self, n: int):
    self.__N = n
    self.nodes = [None] * n
    self.edges = [
      {} for _ in range(n)]


  def add_node_info(
      self,
      v,
      **args):
    self.nodes[v] = Node(**args)


  def add_edge(
      self,
      u, v,
      update=False,
      **args):
    if not update and \
        v in self.edges[u]:
      return
    self.edges[u][v] = Edge(**args)


class MaximumFlow(Graph):
  @abstractmethod
  def maximum_flow(
      self,
      source,
      sink):
    ...


  def minimum_cut(self, **kwargs):
    return self.maximum_flow(
      **kwargs)


class Dinic(MaximumFlow):
  def __init__(self, **kwargs):
    super(Dinic, self) \
      .__init__(**kwargs)


  def bfs(self, source=0) -> None:
    from collections import deque
    n = len(self.nodes)
    self.lv = lv = [None] * n
    lv[source] = 0
    q = deque([source])
    while q:
      u = q.popleft()
      for v, e in \
          self.edges[u].items():
        if e.capacity == 0: continue
        if lv[v] is not None:
          continue
        lv[v] = lv[u] + 1
        q.append(v)


  def flow_to_sink(
        self, u, flow_in):
    if u == self.sink:
      return flow_in
    flow_out = 0
    for v, e in \
        self.edges[u].items():
      if e.capacity == 0: continue
      if self.lv[v] <= self.lv[u]:
        continue
      flow = self.flow_to_sink(
        v,
        min(flow_in, e.capacity),
      )
      if not flow: continue
      self.edges[u][v].capacity \
        -= flow
      if u in self.edges[v]:
        self.edges[v][u].capacity \
          += flow
      else:
        self.add_edge(
          v, u,
          capacity=flow,
        )
      flow_in -= flow
      flow_out += flow
    return flow_out


  def maximum_flow(
      self,
      source,
      sink):
    self.sink = sink
    inf = float('inf')
    flow = 0
    while True:
      self.bfs(source)
      if self.lv[sink] is None:
        return flow
      flow += self.flow_to_sink(
        source, inf)


def solve(n, p, ab):
  g = Dinic(n=n+1)
  for a, b in ab:
    g.add_edge(a, b, capacity=1)
    g.add_edge(b, a, capacity=1)
  for a in p:
    g.add_edge(a, n, capacity=1)
  min_cut = g.maximum_flow(0, n)
  min_cut = g.minimum_cut(
    source=0,
    sink=n,
  )
  print(min_cut)


def main():
  n, _, _ = readline_ints()
  p = readline_ints()
  ab = read_ints()
  ab = zip(*[iter(ab)]*2)
  solve(n, p, ab)


if __name__ == '__main__':
  main()
