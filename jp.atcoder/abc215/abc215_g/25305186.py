import typing



class CompressArray():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    from bisect import bisect_left
    v = sorted(set(a))
    self.__v = v
    return [bisect_left(v, x) for x in a]


  def __getitem__(
    self,
    i: int,
  ) -> int:
    return self.retrieve(i)


  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]



class BinCount():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    c = [0] * (max(a) + 1)
    for x in a: c[x] += 1
    return c


class FlatNonzero():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    return [i for i, x in enumerate(a) if x]



class ModCumprod():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    for i in range(len(a) - 1):
      a[i + 1] *= a[i]
      a[i + 1] %= self.__mod


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod



class ModFactorial():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    a = list(range(n))
    a[0] = 1
    ModCumprod(self.__mod)(a)
    return a


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod


  def inv(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    a = list(range(1, n + 1))
    mod = self.__mod
    a[-1] = pow(self(n)[-1], mod - 2, mod)
    a.reverse()
    ModCumprod(mod)(a)
    return a[::-1]



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
  c: typing.List[int],
) -> typing.NoReturn:
  n = len(c)
  c = CompressArray()(c)
  m = max(c) + 1
  bincount = BinCount()
  c = bincount(bincount(c))
  idx = FlatNonzero()(c)

  mod = 998244353
  choose = ModChoose(mod)

  def count_up(k: int) -> int:
    s = 0
    for i in idx:
      s -= choose(n - i, k) * c[i] % mod
    s %= mod
    s *= choose.inv(n, k)
    return (s + m) % mod

  for k in range(1, n + 1):
    print(count_up(k))


def main() -> typing.NoReturn:
  n = int(input())
  *c, = map(int, input().split())
  solve(c)


main()
