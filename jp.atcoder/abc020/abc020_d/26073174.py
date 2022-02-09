import typing


class FindDivisors():
  def __call__(self, n: int) -> typing.List[int]:
    divs = []
    i = 1
    while i * i < n:
      if n % i:
        i += 1
        continue
      divs.append(i)
      divs.append(n // i)
      i += 1
    if i * i == n: divs.append(i)
    return sorted(divs)


class PrimeFactors():
  def __call__(self, n: int) -> typing.List[int]:
    factors = []
    i = 2
    while i * i <= n:
      if n % i:
        i += 1
        continue
      factors.append(i)
      while n % i == 0: n //= i
    if n > 1: factors.append(n)
    return factors



def solve(n: int, k: int) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  divs = FindDivisors()(k)

  s = dict()
  for d in divs:
    s[d] = (d + n // d * d) * n // d // 2 % mod

  pf = PrimeFactors()(k)
  for p in pf:
    for d in divs:
      if d % p: continue
      s[d // p] -= s[d]
      s[d // p] %= mod


  cnt = 0
  for d in divs:
    cnt += k // d * s[d] % mod
  print(cnt % mod)






def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  solve(n, k)


main()
