import typing



class ReadStdin:
  def __call__(
    self,
  ) -> bytes:
    return next(self.__chunks)


  def __init__(
    self,
  ) -> typing.NoReturn:
    import sys
    self.__buf = (
      sys.stdin.buffer
    )
    self.__chunks = (
      self.__read_chunks()
    )


  def int(
    self,
  ) -> int:
    return int(self())


  def __read_chunks(
    self,
  ) -> typing.Iterator[bytes]:
    while 1:
      l = self.__buf.readline()
      for chunk in l.split():
        yield chunk


  def str(
    self,
  ) -> str:
    b = self()
    return b.decode()


from abc import (
  ABC,
  abstractmethod,
)
import typing



class Solver(
  ABC,
):
  def __call__(
    self,
  ) -> typing.NoReturn:
    self._prepare()
    self._solve()


  def __init__(
    self,
  ) -> typing.NoReturn:
    ...


  @abstractmethod
  def _prepare(
    self,
  ) -> typing.NoReturn:
    ...


  @abstractmethod
  def _solve(
    self,
  ) -> typing.NoReturn:
    ...



import typing
from typing import (
  List,
  Optional,
)
import dataclasses



@dataclasses.dataclass
class Node:
  id_: Optional[int] = None



@dataclasses.dataclass
class Edge:
  id_: Optional[int] = None
  from_ : int = ...
  to: int = ...
  weight: int = 1
  capacity: int = 0



@dataclasses.dataclass
class Graph:
  nodes: List[Node]
  edges: List[List[Edge]]


  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
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
  ) -> typing.NoReturn:
    i = e.from_
    self.edges[i].append(e)


  def add_edges(
    self,
    edges: typing.List[Edge],
  ) -> typing.NoReturn:
    for e in edges:
      self.add_edge(e)


  @property
  def size(
    self,
  ) -> int:
    return len(self.nodes)



import typing
import sys
sys.setrecursionlimit(1 << 22)


@dataclasses.dataclass
class Player():
  first: str
  second: str


class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()
    self.__player = Player(
      first='Takahashi',
      second='Aoki',
    )


  def _prepare(
    self,
  ) -> typing.NoReturn:
    read = self.__read
    h = read.int()
    w = read.int()
    a = b''.join((
      read()
      for _ in range(h)
    )).decode()
    self.__h = h
    self.__w = w
    self.__a = a


  def _solve(
    self,
  ) -> typing.NoReturn:
    self.__preprocess()
    self.__make_graph()
    self.__dfs(0)
    p = self.__player
    s = self.__cache
    print(
      p.first if s[0] > 0
      else p.second if s[0] < 0
      else 'Draw'
    )


  def __dfs(
    self,
    i: int,
  ):
    g = self.__g
    cache = self.__cache
    if cache[i] is not None:
      return
    if not g.edges[i]:
      cache[i] = 0; return
    scores = []
    for e in g.edges[i]:
      j = e.to
      self.__dfs(j)
      scores.append(
        cache[j] + e.weight
      )
    q, r = divmod(i, self.__w)
    rev = (q + r) & 1
    scores.sort(reverse=rev)
    cache[i] = scores[-1]
    return


  def __make_graph(
    self,
  ) -> typing.NoReturn:
    n = self.__n
    h = self.__h
    w = self.__w
    self.__g = Graph(n)
    for i in range(n):
      self.__i = i
      q, r = divmod(i, w)
      self.__rev = (q + r) & 1
      if r < w - 1:
        self.__add_edge(i + 1)
      if q < h - 1:
        self.__add_edge(i + w)


  def __add_edge(
    self,
    j: int,
  ) -> typing.NoReturn:
    c = (
      1 if self.__a[j] == '+'
      else -1
    )
    if self.__rev: c *= -1
    e = Edge(
      from_=self.__i,
      to=j,
      weight=c,
    )
    self.__g.add_edge(e)


  def __preprocess(
    self,
  ) -> typing.NoReturn:
    n = self.__h * self.__w
    score = [None] * n
    self.__n = n
    self.__cache = score



def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()
