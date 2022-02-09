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


class NumpyModular:


  mod: int = None


  def __init__(
    self,
    mod: int,
  ):
    self.mod = mod


  def mat_pow(
    self,
    a: np.ndarray,
    n: int,
  ) -> np.ndarray:
    if n == 0:
      e = np.identity(
        len(a),
        dtype=np.int64,
      )
      return e
    x = self.mat_pow(a, n >> 1)
    x = x.dot(x) % self.mod
    if n & 1:
      x = x.dot(a) % self.mod
    return x


  def inv(self, n: int):
    p = self.mod
    n = int(n)
    return pow(n, p - 2, p)


  def cumprod(self, a):
    l = len(a)
    n = int(np.sqrt(l) + 1)
    a = np.resize(a, (n, n))
    for i in range(n-1):
      a[:, i + 1] *= a[:, i]
      a[:, i + 1] %= self.mod
    for i in range(n-1):
      a[i + 1] *= a[i, -1]
      a[i + 1] %= self.mod
    return np.ravel(a)[:l]


  def factorial(self, n: int):
    fact = np.arange(n)
    fact[0] = 1
    return self.cumprod(fact)


  def inv_factorial(
    self,
    n: int,
  ):
    fact = self.factorial(n)
    ifact = np.arange(1, n + 1)
    ifact[-1] = self.inv(
      fact[-1],
    )
    return self.cumprod(
      ifact[::-1],
    )[n::-1]



mod = 10 ** 9 + 7

class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    n = reader.int()
    m = reader.int()
    k = reader.int()
    a = [
      reader.int()
      for _ in range(n)
    ]
    a = np.array(a)
    xy = [
      reader.int()
      for _ in range(2 * m)
    ]
    xy = np.array(
      xy,
    ).reshape(m, 2) - 1
    self.n = n
    self.m = m
    self.k = k
    self.a = a
    self.xy = xy


  def solve(self):
    self.make_graph()
    np_mod = NumpyModular(mod)
    g = self.g
    k = self.k
    g = np_mod.mat_pow(g, k)
    a = self.a
    a = g.dot(a) % mod
    a = a.astype(int)
    print(*a, sep='\n')



  def make_graph(self):
    n = self.n
    g = np.identity(
      n,
      dtype=np.int64,
    )
    m = self.m
    g *= m * 2
    xy = self.xy
    x, y = xy.T
    np.add.at(g, (x, x), -1)
    np.add.at(g, (y, y), -1)
    np.add.at(g, (x, y), 1)
    np.add.at(g, (y, x), 1)
    b = pow(
      2 * m,
      mod - 2,
      mod,
    )
    g *= b
    g %= mod
    self.g = g



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
