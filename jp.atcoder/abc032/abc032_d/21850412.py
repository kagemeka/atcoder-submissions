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

  M: Final[int] = 1 << 10
  K: Final[int] = 1 << 18


  def prepare(self):
    reader = self.reader
    n = reader.int()
    w = reader.int()
    items = [None] * 2 * n
    for i in range(2 * n):
      items[i] = reader.int()

    items = np.array(
      items,
      dtype=int,
    ).reshape(n, 2)
    self.n = n
    self.w = w
    self.items = items
    self.k = 1 << 18


  def solve(self):
    ptn = self.check_pattern()
    search = eval(
      f'self.search{ptn}',
    )
    print(search())


  def search2(self):
    items = self.items
    w = self.w
    n = items.shape[0]
    a = self.support(
      items[:n//2],
    )
    b = self.support(
      items[n//2:],
    )
    i = np.searchsorted(
      b[:, 1],
      w - a[:, 1],
      'right',
    ) - 1
    a = a[i != -1]
    i = i[i != -1]
    s = a[:, 0] + b[i, 0]
    return s.max()


  def support(
    self,
    items: np.ndarray,
  ):
    n = items.shape[0]
    s = np.arange(1 << n)
    i = np.arange(n)
    s = s[:, None] >> i & 1
    a = (
      items.T[:, None, :] * s
    ).sum(axis=-1).T
    i = np.argsort(a[:, 1])
    a = a[i]
    np.maximum.accumulate(
      a,
      axis=0,
      out=a,
    )
    return a


  def search0(self):
    items = self.items
    w = self.w
    s = items.sum(axis=0)
    if s[1] <= w:
      return s[0]
    dp = np.zeros(
      self.K,
      dtype=int,
    )
    for item in items:
      i, j = item
      np.maximum(
        dp[j:],
        dp[:-j] + i,
        out=dp[j:],
      )
    return dp[w]


  def search1(self):
    items = self.items
    w = self.w
    dp = np.full(
      self.K,
      np.inf,
    )
    dp[0] = 0
    for item in items:
      i, j = item
      np.minimum(
        dp[i:],
        dp[:-i] + j,
        out=dp[i:],
      )
    np.minimum.accumulate(
      dp[::-1],
      out=dp[::-1],
    )
    return np.searchsorted(
      dp,
      w,
      'right',
    ) - 1


  def check_pattern(
    self,
  ) -> int:
    items = self.items
    w = items[:, 1]
    if (w < self.M).all():
      return 0
    v = items[:, 0]
    if (v < self.M).all():
      return 1
    return 2



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
