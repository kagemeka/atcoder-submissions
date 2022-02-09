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

  choku = set((
    'ch',
    'o',
    'k',
    'u',
  ))


  def prepare(self):
    reader = self.reader
    x = reader.str()
    self.x = x


  def solve(self):
    x = self.x
    ok = self.is_choku(
      x,
    )
    print(
      'YES' if ok else 'NO',
    )


  @classmethod
  def is_choku(
    cls,
    s: str,
  ) -> bool:
    choku_tail = cls.choku
    n = len(s)
    if n == 0:
      return True
    if s[-1] in choku_tail:
      return cls.is_choku(
        s[:-1],
      )
    if n == 1:
      return False
    if s[-2:] in choku_tail:
      return cls.is_choku(
        s[:-2],
      )
    return False



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
