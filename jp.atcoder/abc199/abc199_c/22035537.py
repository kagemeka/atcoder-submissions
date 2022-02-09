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
    s = reader.str()
    self.n = n
    self.s = s


  def solve(self):
    reader = self.reader
    q = reader.int()
    self.s = list(self.s)
    self.flg = 0
    for _ in range(q):
      t = reader.int()
      a = reader.int() - 1
      b = reader.int() - 1
      if t == 2:
        self.flg ^= 1
        continue
      self.query(a, b)
    n = self.n
    s = self.s
    if self.flg:
      s = s[n:] + s[:n]
    print(''.join(s))


  def query(
    self,
    a: int,
    b: int,
  ):
    s = self.s
    n = self.n
    m = n * self.flg
    a = (a + m) % (2 * n)
    b = (b + m) % (2 * n)
    s[a], s[b] = s[b], s[a]





def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
