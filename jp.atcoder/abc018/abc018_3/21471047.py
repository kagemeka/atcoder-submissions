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



from \
  scipy \
  .ndimage \
import (
  distance_transform_cdt
  as cdt,
)



class Problem(
  Solver,
):


  def prepare(self):
    reader = self.reader
    (
      r, c, k,
    ) = reader.readline_ints()
    s = reader.read().split()
    *s, = map(list, s)
    s = np.array(s)
    self.r = r
    self.c = c
    self.k = k
    self.s = s
    self.ready = True


  def solve(self):
    assert self.ready
    self.preprocess()
    self.compute_dist()
    s = self.s
    k = self.k
    cnt = np.count_nonzero(
      s >= k,
    )
    print(cnt)


  def compute_dist(
    self,
  ):
    s = self.s
    s = cdt(
      input=s,
      metric='taxicab',
    )
    self.s = s


  def preprocess(
    self,
  ):
    s = self.s
    x = ord(b'x')
    o = ord(b'o')
    s = np.pad(
      array=s,
      pad_width=1,
      mode='constant',
      constant_values=x,
    )
    s = np.where(
      s == o,
      np.inf,
      0,
    )
    self.s = s



def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    p = Problem()
    p()



if __name__ == '__main__':
  main()
