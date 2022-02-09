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

from scipy.sparse.csgraph \
import (
  floyd_warshall,
)

from scipy.sparse import (
  csr_matrix,
)



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    n = reader.int()
    m = reader.int()
    a = [
      reader.int()
      for _ in range(3 * m)
    ]
    a = np.array(
      a,
    ).reshape(m, 3)
    a, b, t = a.T
    self.n, self.m = n, m
    self.a = a - 1
    self.b = b - 1
    self.t = t


  def solve(self):
    self.compute_dist_mat()
    dist = self.dist
    d = dist.max(axis=1).min()
    print(int(d))



  def compute_dist_mat(
    self,
  ):
    n = self.n
    a = self.a
    b = self.b
    t = self.t
    g = csr_matrix(
      (t, (a, b)),
      shape=(n, n),
    )
    dist = floyd_warshall(
      csgraph=g,
      directed=False,
    )
    self.dist = dist



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
