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



class PrimeFactors():
  def __call__(
    self,
    n: int,
  ) -> typing.NoReturn:
    a = []
    p = 2
    while p * p <= n:
      if n % p:
        p += 1
        continue
      a.append(p)
      while not n % p: n //= p
    if n > 1: a.append(n)
    return a



def solve(
  p: int,
) -> typing.NoReturn:
  n = p - 1
  divs = FindDivisors()(n)
  pf = PrimeFactors()(n)

  mod = 998244353
  dp = {
    d: n // d % mod
    for d in divs
  }

  for p in pf:
    for d in divs:
      if d % p: continue
      dp[d // p] -= dp[d]
      dp[d // p] %= mod

  c = 1
  for d in divs:
    c += dp[d] * n // d % mod
    c %= mod
  print(c)



def main() -> typing.NoReturn:
  p = int(input())
  solve(p)



main()
