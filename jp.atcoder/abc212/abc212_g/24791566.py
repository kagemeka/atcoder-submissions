import typing



class FindDivisors():
  def __call__(
    self,
    n: int,
  ) -> typing.List[int]:
    a = []
    i = 1
    while i * i < n:
      if n % i:
        i += 1
        continue
      a.append(i)
      a.append(n // i)
      i += 1
    if i * i == n: a.append(i)
    a.sort()
    return a



class SieveOfEratorthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[bool]:
    s = self.lpf(n)
    for i in range(n):
      s[i] = s[i] == i
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
        s[j] = i
    return s


  def spf(
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
    fn = SieveOfEratorthenes()
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



class EulerTotient():
  def __call__(
    self,
    n: int,
  ) -> int:
    c = n
    for p in self.__pn:
      if p * p > n: break
      if n % p: continue
      c = c // p * (p - 1)
      while not n % p: n //= p
    if n > 1:
      c = c // n * (n - 1)
    return c


  def __init__(
    self,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__pn = PrimeNumbers(n)



def solve(
  p: int,
) -> typing.NoReturn:
  n = p - 1
  divs = FindDivisors()(n)
  euler = EulerTotient(1 << 20)
  mod = 998244353
  c = 1
  for d in divs:
    c += euler(d) * d
    c %= mod
  print(c)


def main() -> typing.NoReturn:
  p = int(input())
  solve(p)


main()
