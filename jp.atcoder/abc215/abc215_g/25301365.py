import typing
import sys
import numpy as np



class ModCumprod():
  def __call__(
    self,
    a: np.array,
  ) -> np.array:
    mod = self.__mod
    n = a.size
    m = int(n ** .5) + 1
    a = np.resize(a, (m, m))
    for i in range(m - 1):
      a[:, i + 1] *= a[:, i]
      a[:, i + 1] %= mod
    for i in range(m - 1):
      a[i + 1] *= a[i, -1]
      a[i + 1] %= mod
    return a.ravel()[:n]


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod



class ModFactorial():
  def __call__(
    self,
    n: int,
  ) -> np.array:
    cumprod = ModCumprod(self.__mod)
    a = np.arange(n)
    a[0] = 1
    return cumprod(a)


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod


  def inv(
    self,
    n: int,
  ) -> np.array:
    mod = self.__mod
    a = np.arange(1, n + 1)
    a[-1] = pow(int(self(n)[-1]), mod - 2, mod)
    return ModCumprod(mod)(a[::-1])[::-1]



class ModChoose():
  def __call__(
    self,
    n: int,
    k: int,
  ) -> int:
    ok = (0 <= k) & (k <= n)
    m = self.__mod
    f, i = self.__fact, self.__ifact
    c = f[n] * i[k] % m * i[n - k] % m
    return c * ok


  def __init__(
    self,
    mod: int,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__mod = mod
    factorial = ModFactorial(mod)
    self.__fact = factorial(n)
    self.__ifact = factorial.inv(n)


  def inv(
    self,
    n: int,
    k: int,
  ) -> int:
    ok = (0 <= k) & (k <= n)
    m = self.__mod
    f, i = self.__fact, self.__ifact
    c = i[n] * f[k] % m * f[n - k] % m
    return c * ok



def solve(
  c: np.array,
) -> typing.NoReturn:
  mod = 998244353

  n = c.size
  a = np.unique(c)
  m = a.size
  c = np.searchsorted(a, c)
  c = np.bincount(np.bincount(c))
  i = np.flatnonzero(c)
  k = np.arange(1, n + 1)[:, None]
  choose = ModChoose(mod)

  upper = choose(n, k) * m - np.sum(
    choose(n - i, k) * c[i],
    axis=1,
  )[:, None] % mod
  upper %= mod
  lower = choose.inv(n, k)

  res = upper * lower % mod
  print(*res.ravel(), sep='\n')


def main() -> typing.NoReturn:
  n = int(input())
  c = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(c)


main()
