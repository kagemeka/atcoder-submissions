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


class EulerTotient():
  def __call__(
    self,
    n: int,
  ) -> int:
    c = n
    p = 2
    while p * p <= n:
      if n % p:
        p += 1
        continue
      c = c // p * (p - 1)
      while not n % p: n //= p
    if n > 1:
      c = c // n * (n - 1)
    return c



def main() -> typing.NoReturn:
  p = int(input())
  n = p - 1
  divs = FindDivisors()(n)
  mod = 998244353
  euler = EulerTotient()
  s = 1
  for d in divs:
    s += euler(d) * d
    s %= mod
  print(s)


main()
