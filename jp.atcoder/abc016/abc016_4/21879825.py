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


from dataclasses import (
  dataclass,
)


@dataclass
class Vector:


  x: int
  y: int


  def cross(
    self,
    other: Vector,
  ) -> int:
    res = self.x * other.y
    res -= self.y * other.x
    return res


  def __add__(
    self,
    other,
  ):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)


  def __neg__(
    self,
  ):
    x = -self.x
    y = -self.y
    return Vector(x, y)


  def __sub__(
    self,
    other,
  ):
    return self + -other



@dataclass
class LineSegment:


  v0: Vector
  v1: Vector


  def intersect(
    self,
    other: LineSegment,
  ) -> bool:
    ok = self.across(other)
    ok &= other.across(self)
    return ok


  def across(
    self,
    other: LineSegment,
  ) -> bool:
    v0 = other.v1 - other.v0
    v1 = self.v0 - other.v0
    v2 = self.v1 - other.v0
    c0 = v0.cross(v1)
    c1 = v0.cross(v2)
    return c0 * c1 <= 0



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    ax = reader.int()
    ay = reader.int()
    bx = reader.int()
    by = reader.int()
    n = reader.int()
    x = [
      reader.int()
      for _ in range(n * 2)
    ]
    x = np.array(
      x,
    ).reshape(n, 2)
    self.ax = ax
    self.ay = ay
    self.bx = bx
    self.by = by
    self.n = n
    self.x = x


  def solve(self):
    self.preprocess()
    s0 = self.s0
    s = self.s
    ok = s0.intersect(s)
    c = np.count_nonzero(ok)
    print(c // 2 + 1)


  def preprocess(
    self,
  ):
    a = Vector(
      self.ax,
      self.ay,
    )
    b = Vector(
      self.bx,
      self.by,
    )
    x = self.x
    x = np.vstack([x, x])
    n = self.n
    p0 = x[:n]
    p1 = x[1:n+1]
    p0 = Vector(*p0.T)
    p1 = Vector(*p1.T)
    s0 = LineSegment(a, b)
    s = LineSegment(p0, p1)
    self.s0 = s0
    self.s = s



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
