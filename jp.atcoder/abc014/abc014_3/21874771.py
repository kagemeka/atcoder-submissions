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

from typing import (
  Final,
)


class Problem(
  Solver,
):

  M: Final[int] = 1 << 20

  def prepare(self):
    reader = self.reader
    n = reader.int()
    a = [
      reader.int()
      for _ in range(2 * n)
    ]
    a = np.array(
      a,
    ).reshape(n, 2)
    a, b = a.T
    self.n = n
    self.a = a
    self.b = b


  def solve(self):
    a, b = self.a, self.b
    m = self.M
    c = np.zeros(m, dtype=int)
    np.add.at(c, a, 1)
    np.add.at(c, b + 1, -1)
    np.cumsum(c, out=c)
    print(c.max())



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
