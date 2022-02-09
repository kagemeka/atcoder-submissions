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



from enum import Enum
from dataclasses import (
  dataclass,
  astuple,
  asdict,
  fields,
  make_dataclass,
)

from typing import (
  NamedTuple,
  Iterable,
  Union,
  Dict,
)

from abc import (
  ABC,
  ABCMeta,
)


# from .. import(
  # Numeric,
# )
Numeric = Union[int, float]

from math import (
  sqrt,
)


@dataclass
class Vector(ABC):

  def __iter__(self):
    return iter(astuple(self))


  def clone(self):
    return self.__class__(
      *self,
    )


  @classmethod
  def vectorize(cls, other):
    t = type(other)
    n = len(fields(cls))
    if t == int or t == float:
      other = cls(*(
        other
        for _ in range(n)
      ))
    if t == tuple:
      assert len(other) == n
      other = cls(*other)
    return other


  def __iadd__(self, other):
    other = self.vectorize(
      other,
    )
    for f in fields(self):
      f = f.name
      a = getattr(self, f)
      b = getattr(other, f)
      a += b
      setattr(self, f, a)
    return self


  def __add__(self, other):
    res = self.clone()
    res += other
    return res


  def __radd__(self, other):
    return self + other


  def __neg__(self):
    return self.__class__(*(
      -getattr(self, f.name)
      for f in fields(self)
    ))


  def __sub__(self, other):
    res = self.clone()
    res += -other
    return res


  def __rsub__(self, other):
    other = self.vectorize(
      other,
    )
    return other - self


  def __imul__(self, other):
    other = self.vectorize(
      other,
    )
    for f in fields(self):
      f = f.name
      a = getattr(self, f)
      b = getattr(other, f)
      a *= b
      setattr(self, f, a)
    return self


  def __mul__(self, other):
    res = self.clone()
    res *= other
    return res


  def __rmul__(self, other):
    return self * other


  def __itruediv__(
    self,
    other,
  ):
    other = self.vectorize(
      other,
    )
    for f in fields(self):
      f = f.name
      a = getattr(self, f)
      b = getattr(other, f)
      a /= b
      setattr(self, f, a)
    return self


  def __truediv__(
    self,
    other,
  ):
    res = self.clone()
    res /= other
    return res


  def __rtruediv__(
    self,
    other,
  ):

    other = self.vectorize(
      other,
    )
    return other / self


  def __ifloordiv__(
    self,
    other,
  ):
    other = self.vectorize(
      other,
    )
    for f in fields(self):
      f = f.name
      a = getattr(self, f)
      b = getattr(other, f)
      a //= b
      setattr(self, f, a)
    return self


  def __floordiv__(
    self,
    other,
  ):
    res = self.clone()
    res //= other
    return res


  def __rfloordiv__(
    self,
    other,
  ):
    other = self.vectorize(
      other,
    )
    return other // self


  def __matmul__(self, other):
    assert (
      other.__class__
      == self.__class__
    )

    res = 0
    for f in fields(self):
      f = f.name
      a = getattr(self, f)
      b = getattr(other, f)
      res += a * b
    return res


  def scale(self, ratio):
    return ratio * self


  @property
  def norm(self):
    s = sum(
      self.asdict().values()
    )
    return sqrt(s)


  def dot(self, other):
    return self @ other


  @classmethod
  def struct(cls, n):
    vector = make_dataclass(
      cls_name='vector',
      fields=[
        (f'x{i}', Numeric, 0)
        for i in range(n)
      ],
      bases=(cls, ),
    )
    return vector


  def asdict(self):
    return asdict(self)


@dataclass
class Vector2D(Vector):
  x: Numeric = 0
  y: Numeric = 0

  def cross_prod(self, other):
    return (
      self.x * other.y
      - self.y * other.x
    )



@dataclass
class Vector3D(Vector):
  x: Numeric = 0
  y: Numeric = 0
  z: Numeric = 0



@dataclass
class Triangle:
  p0: Vector2D
  p1: Vector2D
  p2: Vector2D


  def area(self, sign=True):
    p1 = self.p1 - self.p0
    p2 = self.p2 - self.p0
    s = p1.cross_prod(p2) / 2
    return (
      s if sign else abs(s)
    )



class ABC002C(
  Solver,
):

  def prepare(self):
    reader = self.reader
    (
      x0, y0, x1, y1, x2, y2,
    ) = reader.readline_ints()
    triangle = Triangle(
      p0=Vector2D(x0, y0),
      p1=Vector2D(x1, y1),
      p2=Vector2D(x2, y2),
    )
    self.triangle = triangle
    self.ready = True


  def solve(self):
    assert self.ready
    triangle = self.triangle
    s = triangle.area(
      sign=False,
    )
    print(s)



def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    ABC002C()()


if __name__ == '__main__':
  main()
