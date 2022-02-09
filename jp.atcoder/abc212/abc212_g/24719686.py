from __future__ import (
  annotations,
)

import typing
import abc


class Modular(abc.ABC):

  mod: int

  def __init__(
    self,
    value: int,
  ) -> typing.Noreturn:
    value %= self.mod
    self.__value = value


  def __repr__(self) -> str:
    return f'{self.__value}'


  def __clone(self) -> Modular:
    return self.__class__(
      self.__value,
    )


  @classmethod
  def __to_mod(
    cls,
    rhs: T,
  ) -> Modular:
    if type(rhs) != int:
      return rhs
    return cls(rhs)


  def __add__(
    self,
    rhs: T,
  ) -> Modular:
    x = self.__clone()
    rhs = self.__to_mod(rhs)
    x.__value += rhs.__value
    x.__value %= self.mod
    return x


  def __iadd__(
    self,
    rhs: T,
  ) -> Modular:
    return self + rhs


  def __radd__(
    self,
    lhs: T,
  ) -> Modular:
    return self + lhs


  def __neg__(self) -> Modular:
    return self.__class__(
      -self.__value,
    )


  def __sub__(
    self,
    rhs: T,
  ) -> Modular:
    return self + -rhs


  def __isub__(
    self,
    rhs: T,
  ) -> Modular:
    return self - rhs


  def __rsub__(
    self,
    lhs: T,
  ) -> Modular:
    return -self + lhs


  def __mul__(
    self,
    rhs: T,
  ) -> Modular:
    x = self.__clone()
    rhs = self.__to_mod(rhs)
    x.__value *= rhs.__value
    x.__value %= self.mod
    return x


  def __imul__(
    self,
    rhs: T,
  ) -> Modular:
    return self * rhs


  def __rmul__(
    self,
    lhs: T,
  ) -> Modular:
    return self * lhs


  def __truediv__(
    self,
    rhs: T,
  ) -> Modular:
    rhs = self.__to_mod(rhs)
    return self * rhs.inv()


  def __itruediv__(
    self,
    rhs: T,
  ) -> Modular:
    return self / rhs


  def __rtruediv__(
    self,
    lhs: T,
  ) -> Modular:
    return self.inv() * lhs


  def __floordiv__(
    self,
    rhs: T,
  ) -> Modular:
    return self / rhs


  def __ifloordiv__(
    self,
    rhs: T,
  ) -> Modular:
    return self // rhs


  def __rfloordiv__(
    self,
    lhs: T,
  ) -> Modular:
    return lhs / self


  def __pow__(
    self,
    n: int,
  ) -> Modular:
    return pow(
      self.__value,
      n,
      self.mod,
    )


  def __ipow__(
    self,
    n: int,
  ) -> Modular:
    return self ** n


  def __rpow__(
    self,
    rhs: T,
  ) -> Modular:
    rhs = self.__to_mod(rhs)
    return rhs ** self.__value


  @classmethod
  def mul_identity(
    cls,
  ) -> Modular:
    return cls(1)


  @classmethod
  def add_identity(
    cls,
  ) -> Modular:
    return cls(0)


  def inv(self) -> Modular:
    i = self ** (self.mod - 2)
    return i


  def __eq__(
    self,
    rhs: T,
  ) -> bool:
    rhs = self.__to_mod(rhs)
    return (
      self.__value
      == rhs.__value
    )


  def congruent(
    self,
    rhs: T,
  ) -> bool:
    return self == rhs


T: typing.Type = typing.Union[
  int,
  Modular,
]





import typing



class ModFactory():
  def __call__(
    self,
    modulo: int,
  ) -> Modular:
    class Mint(Modular):
      mod: typing.Final[
        int
      ] = modulo
    return Mint



def find_divisors(
  n: int,
) -> typing.List[int]:
  a = []
  i = 1
  while i * i < n:
    if n % i: i += 1; continue
    a.append(i)
    a.append(n // i)
    i += 1
  if i * i == n: a.append(i)
  a.sort()
  return a



def main() -> typing.NoReturn:
  mod = 998244353
  Mint = ModFactory()(mod)
  p = int(input())
  n = p - 1

  divs = find_divisors(n)[::-1]
  l = len(divs)
  cnt = [
    Mint(0)
    for _ in range(l)
  ]
  for i in range(l):
    d = divs[i]
    c = n // d
    for j in range(i):
      if divs[j] % d: continue
      c -= cnt[j]
    cnt[i] += c

  s = 1
  for i in range(l):
    s += n // divs[i] * cnt[i]
  print(s)


main()
