import typing



from typing import (
  DefaultDict,
)
from collections import (
  defaultdict,
)




class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[bool]:
    s = self.gpf(n)
    for i in range(n):
      s[i] = s[i] == i
    return s


  def gpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      for j in range(i, n, i):
        s[j] = i
    return s


  def lpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      for j in range(i, n, i):
        if s[j] == j: s[j] = i
    return s



class PrimeNumbers():
  def __getitem__(
    self,
    i: int,
  ) -> int:
    return self.__a[i]


  def __init__(
    self,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    fn = SieveOfEratosthenes()
    a = fn(n)
    self.__a = tuple(
      i for i in range(n)
      if a[i]
    )


  def __iter__(
    self,
  ) -> typing.Iterator[int]:
    return iter(self.__a)


  def __repr__(self) -> str:
    return f'{self.__a}'


class PrimeFactorize:
  def __call__(
    self,
    n: int,
  ) -> DefaultDict[int, int]:
    f = defaultdict(int)
    for p in self.__pn:
      if n < 2: return f
      if p * p > n: break
      while n % p == 0:
        f[p] += 1
        n //= p
    f[n] = 1; return f


  def __init__(
    self,
    n: int = 1 << 20,
  ):
    pn = PrimeNumbers(n)
    self.__pn = tuple(pn)


  def factorial(
    self,
    n: int,
  ) -> DefaultDict[int, int]:
    f = defaultdict(int)
    for i in range(n + 1):
      for (
        p, c,
      ) in self(i).items():
        f[p] += c
    return f



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *a, = map(int, input().split())

  fn = PrimeFactorize(1 << 20)
  s = set()

  for x in a:
    for p in fn(x):
      s.add(p)

  cnt = 0
  res = []
  for i in range(1, m + 1):
    primes = fn(i)
    for p in primes:
      if p in s: break
    else:
      cnt += 1
      res.append(i)

  print(cnt)
  print(*res, sep='\n')



main()
