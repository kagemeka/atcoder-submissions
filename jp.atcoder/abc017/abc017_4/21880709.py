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



from abc import (
  ABC,
)


class Modular(ABC):
  mod: int = None


  def __init__(
    self,
    value: int,
  ):
    value %= self.mod
    self.value = value


  def __repr__(
    self,
  ):
    return f'{self.value}'


  def clone(
    self,
  ):
    return self.__class__(
      self.value,
    )


  @classmethod
  def modularize(
    cls,
    other,
  ):
    if type(other) == int:
      return cls(other)
    return other


  def __add__(self, other):
    x = self.clone()
    other = self.modularize(
      other,
    )
    x.value += other.value
    x.value %= self.mod
    return x


  def __iadd__(self, other):
    return self + other


  def __radd__(self, other):
    return self + other


  def __neg__(self):
    return self.__class__(
      -self.value,
    )


  def __sub__(self, other):
    return self + -other


  def __isub__(self, other):
    return self - other


  def __rsub__(self, other):
    return -self + other


  def __mul__(self, other):
    x = self.clone()
    other = self.modularize(
      other,
    )
    x.value *= other.value
    x.value %= self.mod
    return x


  def __imul__(self, other):
    return self * other


  def __rmul__(self, other):
    return self * other


  def __truediv__(self, other):
    other = self.modularize(
      other,
    )
    return self * other.inv()


  def __itruediv__(
    self,
    other,
  ):
    return self / other


  def __rtruediv__(
    self,
    other,
  ):
    return self.inv() * other


  def __pow__(self, n: int):
    if n == 0:
      e = self.mul_identity()
      return e
    a = self ** (n >> 1)
    a *= a
    if n & 1: a *= self
    return a


  def __ipow__(self, n: int):
    return self ** n


  def __rpow__(self, other):
    other = self.modularize(
      other,
    )
    return other ** self.value


  @classmethod
  def mul_identity(cls):
    return cls(1)


  def inv(self):
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
    fact = [
      self.__class__(i)
      for i in range(n)
    ]
    fact = np.array(fact)
    e = self.mul_identity()
    fact[0] = e
    fact.cumprod(out=fact)
    return fact


  def inv_factorial(
    self,
  ):
    fact = self.factorial()
    n = self.value
    ifact = np.arange(
      1,
      n + 1,
    ).astype(object)
    ifact[-1] = fact[-1].inv()
    ifact[::-1].cumprod(
      out=ifact[::-1],
    )
    return ifact


  @classmethod
  def define(
    cls,
    mod: int,
  ):
    class NewModular(
      Modular,
    ):
      pass
    NewModular.mod = mod
    return NewModular



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

from typing import (
  Final,
)


class Problem(
  Solver,
):


  MOD: Final[int] = 10 ** 9 + 7
  mint = Modular.define(
    mod = MOD,
  )


  def prepare(self):
    reader = self.reader
    n = reader.int()
    m = reader.int()
    f = [
      reader.int() - 1
      for _ in range(n)
    ]
    self.n = n
    self.m = m
    self.f = f


  def solve(self):
    self.preprocess()
    n = self.n
    mint = self.mint
    dp = [
      mint(0)
      for _ in range(n + 1)
    ]
    dp[0] += 1

    prev = self.prev
    self.l = 0
    self.s = dp[0]
    self.dp = dp
    for i in range(n):
      self.proceed(prev[i])
      dp[i + 1] = self.s
      self.s += self.s
    print(dp[-1])


  def proceed(
    self,
    i: int,
  ):
    if i is None:
      return
    while self.l <= i:
      self.s -= self.dp[self.l]
      self.l += 1


  def preprocess(
    self,
  ):
    n = self.n
    prev = [None] * n
    f = self.f
    m = self.m
    cache = [None] * m
    for i in range(n):
      x = f[i]
      prev[i] = cache[x]
      cache[x] = i
    self.prev = prev



def main():
  t = 1
  # t = StdReader().int()
  for _ in range(t):
    Problem()()



if __name__ == '__main__':
  main()
