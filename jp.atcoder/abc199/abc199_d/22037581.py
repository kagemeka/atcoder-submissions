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


class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    n = reader.int()
    m = reader.int()
    a = [
      reader.int()
      for _ in range(2 * m)
    ]
    a = np.array(
      a,
    ).reshape(m, 2) - 1
    self.n = n
    self.m = m
    self.a = a


  def solve(self):
    self.make_graph()
    n = self.n
    self.cnt = [3] * n
    self.cnt[0] = 3
    self.visited = [False] * n
    self.order = [None] * n
    self.o = 0
    self.dfs(0)
    cnt = self.cnt
    s = 1
    for i in range(n):
      s *= max(cnt[i], 0)
    print(s)




  def make_graph(self):
    a = self.a
    n = self.n
    g = [[] for _ in range(n)]
    for x, y in a:
      g[x].append(y)
      g[y].append(x)

    self.g = g

  def dfs(
    self,
    i: int,
  ):
    g = self.g
    to = g[i]
    visited = self.visited
    visited[i] = True
    self.order[i] = self.o
    self.o += 1
    for j in to:
      if visited[j]:
        if (
          self.order[j]
          > self.order[i]
        ):
          continue
        self.cnt[i] -= 1
        continue
      self.dfs(j)



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
