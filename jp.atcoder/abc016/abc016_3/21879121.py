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
      for _ in range(m * 2)
    ]
    a = np.array(
      a,
    ).reshape(m, 2) - 1
    a, b = a.T
    self.n = n
    self.m = m
    self.a = a
    self.b = b


  def solve(self):
    self.make_graph()
    n = self.n
    for i in range(n):
      self.query(i)


  def query(
    self,
    i: int,
  ) -> None:
    g = self.g
    f = g[i]
    ff = g[f].sum(axis=0)
    ff = np.count_nonzero(ff)
    print(ff - 1)


  def make_graph(
    self,
  ):
    a, b = self.a, self.b
    n = self.n
    g = np.zeros(
      (n, n),
      dtype=bool,
    )
    g[a, b] = True
    g += g.T
    self.g = g



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
