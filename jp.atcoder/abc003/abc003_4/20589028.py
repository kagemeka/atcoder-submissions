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
)
from typing import (
  Union,
)
import numpy as np


class Modulus(Enum):
  MOD0 = 10**4 + 7
  MOD1 = 998_244_353
  MOD2 = 10**9 + 7
  MOD3 = 10**9 + 9


class ModularInt:
  def __init__(
    self,
    value: int=0,
    modulus: Union[
      Modulus,
      int,
    ]=(
      Modulus.MOD2
    ),
  ):

    self.mod: int = modulus
    self.value: int = value


  @property
  def mod(self):
    return self.modulus


  @mod.setter
  def mod(self, v):
    if type(v) == Modulus:
      v = v.value
    self.modulus = v


  @property
  def value(self):
    return self._value


  @value.setter
  def value(self, v):
    assert type(v) == int
    self._value = v % self.mod


  @value.deleter
  def value(self):
    del self._value


  def __repr__(self) -> str:
    return f'{self.value}'


  def clone(self):
    return self.__class__(
      self.value,
      self.mod,
    )


  def modularize(self, other):
    if (
      type(other) != ModularInt
    ):
      other = self.__class__(
        int(other),
        self.mod,
      )
    return other


  def __iadd__(self, other):
    other = self.modularize(
      other,
    )
    self.value += other.value
    self.value %= self.mod
    return self


  def __add__(self, other):
    res = self.clone()
    res += other
    return res


  def __radd__(self, other):
    return self + other


  def __neg__(self):
    return self.modularize(
      -self.value,
    )


  def __sub__(self, other):
    res = self.clone()
    res += -other
    return res


  def __rsub__(self, other):
    other = self.modularize(
      other,
    )
    return other - self


  def __imul__(self, other):
    other = self.modularize(
      other,
    )
    self.value *= other.value
    self.value %= self.mod
    return self


  def __mul__(self, other):
    res = self.clone()
    res *= other
    return res


  def __rmul__(self, other):
    return self * other


  def __truediv__(self, other):
    other = self.modularize(
      other,
    )
    res = self.clone()
    res *= other.invert()
    return res


  def __rtruediv__(
    self,
    other,
  ):
    other = self.modularize(
      other,
    )
    return other / self


  def __floordiv__(
    self,
    other,
  ):
    return self / other


  def __rfloordiv__(
    self,
    other,
  ):
    return other / self


  def pow(self, n):
    if n == 0:
      return self.modularize(1)
    a = self.pow(n >> 1)
    a *= a
    if n & 1: a *= self
    return a


  def __ipow__(self, other):
    other = self.modularize(
      other,
    )

    self.value = pow(
      self.value,
      other.value,
      self.mod,
    )
    return self


  def __pow__(self, other):
    res = self.clone()
    res **= other
    return res


  def __rpow__(self, other):
    other = self.modularize(
      other,
    )
    return other ** self


  def invert(self):
    i = self ** (self.mod - 2)
    return i


  def __eq__(self, other):
    other = self.modularize(
      other,
    )
    return (
      self.value == other.value
    )


  def congruent(
    self,
    other,
  ):
    return self == other


  def factorial(
    self,
  ):
    n = self.value
    fact = range(n + 1)
    fact: (
      np.ndarray
    ) = np.array((
      *map(
        ModularInt,
        fact,
      ),
    ))
    fact[0] = ModularInt(
      1,
      self.mod,
    )
    fact.cumprod(out=fact)
    return fact


  def inverse_factorial(
    self,
  ):
    fact = self.factorial()
    inv_fact: (
      np.ndarray
    ) = np.arange(
      1, fact.size + 1,
    ).astype(object)
    inv_fact[-1] = (
      fact[-1].invert()
    )
    inv_fact[::-1].cumprod(
      out=inv_fact[::-1]
    )
    return inv_fact

Mint = ModularInt



class ChooseMod(
  Mint,
):
  def __init__(
    self,
    n: int=1 << 20,
    *args,
    **kwargs,
  ):
    super().__init__(
      value=n,
      *args,
      **kwargs,
    )
    (
      self.fact,
      self.inv_fact,
    ) = (
      self.factorial(),
      self.inverse_factorial(),
    )


  def __call__(self, n, r):
    return self.choose(n, r)


  def choose(
    self,
    n: int,
    r: int,
  ):
    bl = (0 <= r) & (r <= n)
    p = self.mod
    return (
      bl * self.fact[n]
      * self.inv_fact[r]
      * self.inv_fact[n - r]
    )


class ABC003D_0(
  Solver,
):

  def prepare(self):
    reader = self.reader
    (
      r, c, y, x, d, l,
    ) =  reader.read_ints()
    (
      self.r,
      self.c,
      self.y,
      self.x,
      self.d,
      self.l,
    ) = (
      r, c, y, x, d, l,
    )
    self.choose = ChooseMod(
      n=1 << 10,
      modulus=Modulus.MOD2,
    )
    self.ready = True


  def solve(self):
    assert self.ready
    (
      r, c, y, x,
    ) = (
      self.r,
      self.c,
      self.y,
      self.x,
    )
    blocks = (
      (r - y + 1)
      * (c - x + 1)
    )
    c = self.count(y, x)
    c -= self.count(y-1, x) * 2
    c -= self.count(y, x-1) * 2
    c += self.count(y-2, x)
    c += self.count(y, x-2)
    c += self.count(y-1, x-1)*4
    c -= self.count(y-2, x-1)*2
    c -= self.count(y-1, x-2)*2
    c += self.count(y-2, x-2)
    res = blocks * c
    print(res)


  def count(self, y, x):
    d, l = self.d, self.l
    if y <= 0 or x <= 0:
      return 0
    if y * x < d + l:
      return 0
    c = (
      self.choose(y*x, d+l)
      * self.choose(d+l, d)
    )
    return c



def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    ABC003D_0()()


if __name__ == '__main__':
  main()
