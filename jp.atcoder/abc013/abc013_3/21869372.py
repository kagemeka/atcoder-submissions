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
    h = reader.int()
    a = reader.int()
    b = reader.int()
    c = reader.int()
    d = reader.int()
    e = reader.int()
    self.n = n
    self.h = h
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e


  def solve(self):
    n = self.n
    h = self.h
    a = self.a
    b = self.b
    c = self.c
    d = self.d
    e = self.e

    x = np.arange(n + 1)
    num = (
      n * e - h - (b + e) * x
    )
    den = d + e
    y = num // den + 1
    np.maximum(y, 0, out=y)
    y = np.minimum(
      y,
      n - x,
      out=y,
    )
    mn = np.amin(a * x + c * y)
    print(mn)



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
