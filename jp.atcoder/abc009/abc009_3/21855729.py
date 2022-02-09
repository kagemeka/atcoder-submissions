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

from heapq import (
  heappush,
  heappop,
)


from dataclasses import (
  dataclass,
)


@dataclass
class Item:


  char: str
  index: int
  cost: int


  def __lt__(
    self,
    other: Item,
  ) -> bool:
    if self.char != other.char:
      return (
        self.char < other.char
      )
    if self.cost != other.cost:
      return (
        self.cost < other.cost
      )
    return (
      self.index > other.index
    )



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    n = reader.int()
    k = reader.int()
    s = list(reader.str())
    self.n = n
    self.k = k
    self.s = s


  def solve(self):
    s = self.s
    n = self.n
    self.cost = [1] * n
    for i in range(n):
      self.i = i
      self.search()
      self.update()
    print(''.join(s))


  def search(self):
    i = self.i
    s = self.s
    n = self.n
    cost = self.cost
    h = []
    c0 = s[i]
    for j in range(i + 1, n):
      c = s[j]
      if c >= c0:
        continue
      cst = cost[i] + cost[j]
      if cst > self.k:
        continue
      item = Item(
        char=c,
        index=j,
        cost=cst,
      )
      heappush(h, item)
    self.heap = h


  def update(self):
    i = self.i
    h = self.heap
    if not h: return
    item = heappop(h)
    j = item.index
    self.k -= item.cost
    self.swap(i, j)
    cost = self.cost
    cost[i] = cost[j] = 0


  def swap(
    self,
    i: int,
    j: int,
  ) -> None:
    s = self.s
    s[i], s[j] = s[j], s[i]



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
