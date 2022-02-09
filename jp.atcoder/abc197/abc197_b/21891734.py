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
    h = reader.int()
    w = reader.int()
    x = reader.int()
    y = reader.int()
    s = [
      list(reader.str())
      for _ in range(h)
    ]
    s = np.array(s, dtype='U1')
    self.h = h
    self.w = w
    self.x = x
    self.y = y
    self.s = s


  def solve(self):
    self.preprocess()
    s = self.s
    x, y = self.x, self.y
    print(s[x, y])


  def preprocess(
    self,
  ):
    s = self.s
    a = np.zeros(
      s.shape,
    )
    a[s == '.'] = np.inf
    a = np.pad(
      a,
      (1, 1),
    )
    h, w = self.h, self.w
    u = a.copy()
    u = self.cummin(u)
    d = a.copy()[::-1]
    d = self.cummin(d)[::-1]
    l = a.copy().T
    l = self.cummin(l).T
    r = a.copy().T[::-1]
    r = self.cummin(r)[::-1].T
    s = u + d + l + r
    np.maximum(
      s - 3,
      0,
      out=s,
    )
    self.s = s.astype(int)


  def cummin(
    self,
    a: np.ndarray,
  ):
    n = a.shape[0]
    for i in range(n - 1):
      np.minimum(
        a[i + 1],
        a[i] + 1,
        out=a[i + 1],
      )
    return a



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
