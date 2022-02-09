import typing
import collections



class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    assert n > 1
    s = self.gpf(n)
    for i in range(n):
      s[i] = s[i] == i
    return s


  def gpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    assert n > 1
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
    assert n > 1
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
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = SieveOfEratosthenes()(n)
    return [i for i in range(n) if s[i]]



class PrimeFactorize():
  def __call__(
    self,
    n: int,
  ) -> typing.DefaultDict[int, int]:
    f = collections.defaultdict(int)
    for p in self.__pn:
      if p * p > n: break
      while n % p == 0:
        n //= p
        f[p] += 1
    if n > 1: f[n] = 1
    return f


  def __init__(
    self,
    max_n: int = 1 << 40,
  ) -> typing.NoReturn:
    n = 1
    while n * n <= max_n:
      n <<= 1
    self.__pn = PrimeNumbers()(n)


  def factorial(
    self,
    n: int,
  ) -> typing.List[int]:
    f = collections.defaultdict(int)
    for i in range(n + 1):
      for p, c in self(i).items():
        f[p] += c
    return f



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *a, = map(int, input().split())

  fn = PrimeFactorize(max_n=1 << 20)

  p = [False] * (1 << 20)
  for x in a:
    for i in fn(x): p[i] = True

  s = [True] * (m + 1)
  s[0] = False
  for i in range(m + 1):
    if not p[i] or not s[i]: continue
    for j in range(i, m + 1, i):
      s[j] = False
  print(sum(s))
  for i in range(m + 1):
    if s[i]: print(i)


main()
