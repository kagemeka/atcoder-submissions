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
    d = reader.int()
    a = [
      reader.int() - 1
      for _ in range(m)
    ]
    self.n = n
    self.m = m
    self.d = d
    self.a = a


  def solve(self):
    self.solve_ghost_leg()
    self.doubling()
    res = self.a + 1
    print(*res, sep='\n',)


  def doubling(
    self,
  ):
    a = self.a
    d = self.d
    a = self.pow(a, d)
    self.a = a


  def pow(
    self,
    a: np.ndarray,
    n: int,
  ) -> np.ndarray:
    if n == 0:
      return self.identity()
    x = self.pow(a, n >> 1)
    x = x[x]
    if n & 1:
      x = x[a]
    return x


  def identity(
    self,
  ):
    n = self.n
    return np.arange(n)


  def solve_ghost_leg(
    self,
  ):
    a = self.a
    n = self.n
    b = list(range(n))
    for i in a[::-1]:
      j = i + 1
      b[i], b[j] = b[j], b[i]
    a = np.array(b)
    self.a = a



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
