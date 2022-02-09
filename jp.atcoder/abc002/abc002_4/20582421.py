from dataclasses import (
  dataclass,
  asdict,
  astuple,
  field,
)

import numpy as np
import sys

from typing import (
  List,
)

from abc import (
  ABC,
  abstractmethod,
)


class Reader:

  @staticmethod
  def readline() -> bytes:
    return (
      sys.stdin.buffer
      .readline()
      .rstrip()
    )


  @classmethod
  def read_int(cls) -> int:
    ln = cls.readline()
    return int(ln)


  @classmethod
  def read_str(cls) -> str:
    ln = cls.readline()
    return ln.decode()


  @classmethod
  def readline_ints(
    cls,
  ) -> List[int]:
    *ints, = map(
      int,
      cls.readline().split(),
    )
    return ints


  @classmethod
  def readline_strs(
    cls,
  ) -> List[str]:
    return (
      cls.read_str()
      .split()
    )


  @staticmethod
  def read() -> bytes:
    return (
      sys.stdin.buffer
      .read()
    )


  @classmethod
  def read_ints(
    cls,
  ) -> List[int]:
    *ints, = map(
      int,
      cls.read().split(),
    )
    return ints


  @classmethod
  def read_strs(
    cls,
  ) -> List[str]:
    return (
      cls.read()
      .decode()
      .split()
    )


  @staticmethod
  def readlines(
  )  -> List[bytes]:
    lines = (
      sys.stdin.buffer
      .readlines()
    )
    lines = [
      l.rstrip()
      for l in lines
    ]
    return lines



class NumpyReader(Reader):

  @classmethod
  def readline_ints(
    cls,
  ) -> np.array:
    return np.fromstring(
      string=cls.read_str(),
      dtype=np.int64,
      sep=' ',
    )


  @classmethod
  def read_ints(
    cls,
  ) -> np.array:
    return np.fromstring(
      string=cls.read() \
        .decode(),
      dtype=np.int64,
      sep=' ',
    )



class Solver(ABC):

  def __init__(self):
    self.reader = Reader()
    self.np_reader = (
      NumpyReader()
    )
    self.ready = False


  def __call__(
    self,
    *args,
    **kwargs,
  ):
    self.run(
      *args,
      **kwargs,
    )


  def run(self):
    self.prepare()
    self.solve()


  @abstractmethod
  def prepare(self):
    ...
    self.ready = True



  @abstractmethod
  def solve(self):
    assert self.ready
    ...


def bit_count(n):
  cnt = 0
  l = n.bit_length()
  for _ in range(l):
    cnt += n & 1
    n >>= 1
  return cnt


class ABC002D(
  Solver,
):

  def prepare(self):
    reader = self.reader
    (
      n, m, *xy,
    ) = reader.read_ints()
    xy = np.array(
      xy,
    ).reshape(m, 2) - 1
    relations = [
      1 << i
      for i in range(n)
    ]
    for x, y in xy:
      relations[x] |= 1 << y
      relations[y] |= 1 << x

    self.relations = relations
    self.n = n
    self.ready = True


  def solve(self):
    assert self.ready
    n = self.n
    relations = self.relations

    c = 0
    for s in range(1 << n):
      t = s
      for i in range(n):
        if ~s >> i & 1:
          continue
        t &= relations[i]
      if t != s: continue
      c = max(
        c,
        bit_count(s),
      )
    print(c)


def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    ABC002D()()


if __name__ == '__main__':
  main()
