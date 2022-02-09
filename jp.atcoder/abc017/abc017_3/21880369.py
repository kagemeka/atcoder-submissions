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
      for _ in range(n * 3)
    ]
    a = np.array(
      a,
    ).reshape(n, 3)
    l, r, s = a.T
    l -= 1; r -= 1
    self.n = n
    self.m = m
    self.l = l
    self.r = r
    self.s = s


  def solve(self):
    l, r = self.l, self.r
    s = self.s
    a = np.zeros(
      1 << 20,
      dtype=int,
    )
    np.add.at(a, l, s)
    np.add.at(a, r + 1, -s)
    np.cumsum(a, out=a)
    tot = s.sum()
    m = self.m
    mx = tot - a[:m].min()
    print(mx)



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
