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


@dataclass
class Time:
  start: int
  end: int

  # @property
  def round_(self):
    s, e = (
      self.start,
      self.end,
    )

    s = s // 5 * 5
    e = (e + 4) // 5 * 5
    return self.__class__(
      start=s,
      end=e,
    )

  @classmethod
  def from_str(
    cls,
    t: str,
  ):
    se = map(
      int,
      t.split('-'),
    )
    se = map(
      cls.to_minutes,
      se,
    )
    return cls(*se)


  def __repr__(
    self,
  ):
    s, e = map(
      self.to_hmform,
      [*self],
    )
    return f'{s:04}-{e:04}'


  @staticmethod
  def to_minutes(t):
    q, r = divmod(t, 100)
    return 60 * q + r


  @staticmethod
  def to_hmform(t):
    q, r = divmod(t, 60)
    return 100 * q + r


  def __iter__(self):
    return iter(
      astuple(self),
    )




class ProblemName(
  Solver,
):

  def prepare(self):
    reader = self.reader
    n = reader.read_int()
    self.n = n
    m = 24 * 60 + 1
    term = [0] * (m + 1)
    for _ in range(n):
      t = reader.read_str()
      t = Time.from_str(t)
      t = t.round_()
      term[t.start] += 1
      term[t.end + 1] -= 1

    for i in range(m):
      term[i + 1] += term[i]

    self.term = term
    self.m = m

    self.ready = True


  def solve(self):
    assert self.ready
    n, m = self.n, self.m
    term = self.term

    res = []
    raining = False
    for i in range(m + 1):
      if term[i]:
        if raining:
          continue
        s = i
        raining = True
      elif raining:
        e = i - 1
        res.append(
          Time(
            start=s,
            end=e,
          )
        )
        raining = False
      else:
        pass

    for t in res:
      print(t)



def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    ProblemName()()


if __name__ == '__main__':
  main()
