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
class Wind:
  deg: int
  dist: int

  dir_ = [
    'NNE',
    'NE',
    'ENE',
    'E',
    'ESE',
    'SE',
    'SSE',
    'S',
    'SSW',
    'SW',
    'WSW',
    'W',
    'WNW',
    'NW',
    'NNW',
    'N',
  ]

  @property
  def speed(self):
    return self.dist / 60


  @property
  def force(self):
    s = round(self.speed, 2)
    return (
      0 if 0.0 <= s < 0.25
      else 1 if (
        0.25 <= s < 1.55
      ) else 2 if (
        1.55 <= s < 3.35
      ) else 3 if (
        3.35 <= s < 5.45
      ) else 4 if (
        5.45 <= s < 7.95
      ) else 5 if (
        7.95 <= s < 10.75
      ) else 6 if (
        10.75 <= s < 13.85
      ) else 7 if (
        13.85 <= s < 17.15
      ) else 8 if (
        17.15 <= s < 20.75
      ) else 9 if (
        20.75 <= s < 24.45
      ) else 10 if (
        24.45 <= s < 28.45
      ) else 11 if (
        28.45 <= s < 32.65
      ) else 12
    )


  @property
  def direction(self):
    f = self.force
    if f == 0:
      return 'C'

    deg = self.deg * 10
    i = (deg - 1125) // 2250
    print(i)
    return self.dir_[i]


class ABC001C_0(
  Solver,
):

  def prepare(self):
    reader = self.reader
    (
      deg,
      dis,
    ) = reader.readline_ints()
    self.wind = Wind(
      deg=deg,
      dist=dis,
    )
    self.ready = True


  def solve(self):
    assert self.ready
    wind = self.wind
    f = wind.force
    d = wind.direction
    print(d, f, sep=' ')



def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    ABC001C_0()()


if __name__ == '__main__':
  main()
