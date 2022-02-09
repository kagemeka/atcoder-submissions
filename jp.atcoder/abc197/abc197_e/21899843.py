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
    a = [
      reader.int()
      for _ in range(2 * n)
    ]
    a = np.array(
      a,
    ).reshape(n, 2)
    a[:, 1] -= 1
    self.n = n
    self.a = a


  def solve(self):
    self.preprocess()
    a = self.a
    n = self.n
    dist = np.zeros(
      (n, 2),
      dtype=int,
    )
    for i in range(n - 1):
      d = dist[i]
      x = a[i]
      y = a[i + 1]
      d = d + np.abs(
        y[:, None] - x,
      )
      d = d.min(axis=1)
      d += y[1] - y[0]
      dist[i + 1] = d[::-1]
    print(dist[-1, 0])


  def preprocess(
    self,
  ):
    a = self.a
    n = self.n
    a = a[np.argsort(a[:, 0])]
    a = a[np.argsort(a[:, 1])]
    i = np.arange(n)
    ids = a[:, 1]
    l = np.searchsorted(
      ids,
      i,
      'left',
    )
    r = np.searchsorted(
      ids,
      i,
      'right',
    )
    i = np.flatnonzero(l != r)
    i = l != r
    i = np.vstack(
      (l, r - 1),
    ).T[i]
    a = a[:, 0][i]
    a = np.pad(
      a,
      ((1, 1), (0, 0)),
    )
    self.a = a
    self.n = a.shape[0]



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
