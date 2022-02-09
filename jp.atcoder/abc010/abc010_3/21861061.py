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
class Message:
  ok: str
  ng: str


class Problem(
  Solver,
):

  MSG = Message(
    'YES',
    'NO',
  )


  def prepare(self):
    reader = self.reader
    sx = reader.int()
    sy = reader.int()
    gx = reader.int()
    gy = reader.int()
    t = reader.int()
    v = reader.int()
    n = reader.int()
    a = [
      reader.int()
      for _ in range(2 * n)
    ]
    a = np.array(
      a,
    ).reshape(n, 2)
    s = np.array([sx, sy])
    g = np.array([gx, gy])
    self.s = s
    self.g = g
    self.t = t
    self.t = t
    self.v = v
    self.a = a


  def solve(self):
    a = self.a
    s = self.s
    g = self.g
    d0 = np.linalg.norm(
      a - s,
      axis=1,
    )
    d1 = np.linalg.norm(
      g - a,
      axis=1,
    )
    d = d0 + d1
    v, t = self.v, self.t
    possible = np.any(
      d <= v * t,
    )
    msg = self.MSG
    ans = (
      msg.ok if possible
      else msg.ng
    )
    print(ans)



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
