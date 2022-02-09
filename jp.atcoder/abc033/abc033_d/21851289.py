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

  EPS: Final[float] = 1e-10


  def prepare(self):
    reader = self.reader
    n = reader.int()
    polygon = [None] * 2 * n
    for i in range(2 * n):
      polygon[i] = reader.int()
    polygon = np.array(
      polygon,
    ).reshape(n, 2)
    self.n = n
    self.polygon = polygon


  def solve(self):
    n = self.n
    polygon = self.polygon
    self.right = 0
    self.obtuse = 0
    for i in range(n):
      j = np.arange(n - 1)
      j[i:] += 1
      a = polygon[j]
      a -= polygon[i]
      self.a = a
      self.count_up()
    r = self.right
    o = self.obtuse
    a = n * (n - 1) * (n - 2)
    a //= 6
    a -= r + o
    print(a, r, o)


  def count_up(self):
    e = self.EPS
    a = self.a
    x, y = a.T
    args = np.arctan2(y, x)
    args.sort()
    a = np.hstack((
      args,
      args + 2 * np.pi,
    ))
    l = np.searchsorted(
      a,
      args + np.pi / 2 - e,
      'right',
    )
    c = np.searchsorted(
      a,
      args + np.pi / 2 + e,
      'right',
    )
    r = np.searchsorted(
      a,
      args + np.pi - e,
      'right',
    )
    self.right += np.sum(
      c - l,
    )
    self.obtuse += np.sum(
      r - c,
    )



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
